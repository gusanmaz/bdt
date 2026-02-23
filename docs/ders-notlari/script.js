/* =============================================
   Büyük Veri Teknolojileri - Ders Notları
   Ortak JavaScript Dosyası
   Pyodide + Tema + Syntax Highlight + TOC
   ============================================= */

// ─── Theme Management ───
function initTheme() {
  const saved = localStorage.getItem('bvt-theme');
  if (saved) {
    document.documentElement.setAttribute('data-theme', saved);
  } else if (window.matchMedia('(prefers-color-scheme: dark)').matches) {
    document.documentElement.setAttribute('data-theme', 'dark');
  }
  updateThemeButton();
}

function toggleTheme() {
  const current = document.documentElement.getAttribute('data-theme');
  const next = current === 'dark' ? 'light' : 'dark';
  document.documentElement.setAttribute('data-theme', next);
  localStorage.setItem('bvt-theme', next);
  updateThemeButton();
  // Re-render mermaid if present
  if (window.mermaid) {
    document.querySelectorAll('.mermaid').forEach(el => {
      el.removeAttribute('data-processed');
    });
    mermaid.init(undefined, '.mermaid');
  }
}

function updateThemeButton() {
  const btn = document.querySelector('.theme-toggle');
  if (!btn) return;
  const isDark = document.documentElement.getAttribute('data-theme') === 'dark';
  btn.innerHTML = isDark ? '☀️ Açık Mod' : '🌙 Koyu Mod';
}

// ─── Build Code Blocks (uses Highlight.js) ───
function buildCodeBlocks() {
  // Map our data-lang values to highlight.js language names
  const langMap = {
    'python': 'python', 'py': 'python',
    'json': 'json',
    'sql': 'sql',
    'bash': 'bash', 'shell': 'bash', 'sh': 'bash',
    'csv': 'plaintext', 'text': 'plaintext'
  };

  document.querySelectorAll('.code-block').forEach(block => {
    const pre = block.querySelector('pre');
    const codeEl = pre?.querySelector('code');
    if (!codeEl) return;

    const lang = block.dataset.lang || 'text';
    const raw = codeEl.textContent;

    // Store raw code first
    block.dataset.raw = raw;

    // Apply highlight.js
    const hljsLang = langMap[lang.toLowerCase()] || 'plaintext';
    codeEl.className = `language-${hljsLang}`;
    if (window.hljs) {
      hljs.highlightElement(codeEl);
    }

    // Add line numbers by wrapping each line
    const highlighted = codeEl.innerHTML;
    const lines = highlighted.split('\n');
    // Remove trailing empty line if exists
    if (lines.length > 0 && lines[lines.length - 1].trim() === '') lines.pop();
    const wrappedLines = lines.map(line =>
      `<span class="line">${line || '\u00A0'}</span>`
    ).join('\n');
    codeEl.innerHTML = wrappedLines;
    pre.classList.add('line-numbers');

    // Build header
    const header = block.querySelector('.code-header');
    if (!header) {
      const h = document.createElement('div');
      h.className = 'code-header';
      h.innerHTML = `
        <span class="code-lang lang-${lang}">${lang}</span>
        <div class="code-actions">
          <button onclick="copyCode(this)" title="Kopyala">📋 Kopyala</button>
          ${(lang === 'python' || lang === 'py') ? `<button onclick="runCode(this)" title="Çalıştır" class="run-btn">▶️ Çalıştır</button>` : ''}
        </div>
      `;
      block.insertBefore(h, pre);
    }
  });
}

// ─── Copy Code ───
function copyCode(btn) {
  const block = btn.closest('.code-block');
  const raw = block.dataset.raw;
  navigator.clipboard.writeText(raw).then(() => {
    btn.classList.add('copied');
    btn.innerHTML = '✅ Kopyalandı!';
    setTimeout(() => {
      btn.classList.remove('copied');
      btn.innerHTML = '📋 Kopyala';
    }, 2000);
  });
}

// ─── Pyodide (Run Python in Browser) ───
let pyodideInstance = null;
let pyodideLoading = false;

async function loadPyodide_() {
  if (pyodideInstance) return pyodideInstance;
  if (pyodideLoading) {
    // Wait for it
    while (pyodideLoading) await new Promise(r => setTimeout(r, 200));
    return pyodideInstance;
  }
  pyodideLoading = true;
  updatePyodideStatus('Yükleniyor...');
  try {
    pyodideInstance = await loadPyodide({
      indexURL: 'https://cdn.jsdelivr.net/pyodide/v0.24.1/full/'
    });
    // Pre-load common packages
    await pyodideInstance.loadPackage(['micropip']);
    pyodideLoading = false;
    updatePyodideStatus('Hazır ✓');
    document.querySelector('.pyodide-status')?.classList.add('ready');
    return pyodideInstance;
  } catch (e) {
    pyodideLoading = false;
    updatePyodideStatus('Hata!');
    console.error('Pyodide yüklenemedi:', e);
    return null;
  }
}

function updatePyodideStatus(text) {
  const el = document.querySelector('.pyodide-status .status-text');
  if (el) el.textContent = text;
}

async function runCode(btn) {
  const block = btn.closest('.code-block');
  const raw = block.dataset.raw;

  // Show loading
  btn.innerHTML = '⏳ Çalışıyor...';
  btn.disabled = true;

  // Get or create output area
  let outputDiv = block.querySelector('.run-output');
  if (!outputDiv) {
    outputDiv = document.createElement('div');
    outputDiv.className = 'run-output';
    block.appendChild(outputDiv);
  }

  try {
    const pyodide = await loadPyodide_();
    if (!pyodide) {
      outputDiv.innerHTML = '<span class="output-label">Hata</span><span class="output-error">Pyodide yüklenemedi. Sayfayı yenileyin.</span>';
      outputDiv.classList.add('visible');
      return;
    }

    // Capture stdout
    pyodide.runPython(`
import sys, io
sys.stdout = io.StringIO()
sys.stderr = io.StringIO()
    `);

    try {
      // Auto-detect and load required packages
      const imports = raw.match(/^\s*import\s+(\w+)|^\s*from\s+(\w+)/gm);
      if (imports) {
        const pkgMap = { 'pandas': 'pandas', 'numpy': 'numpy', 'matplotlib': 'matplotlib', 'scipy': 'scipy', 'sklearn': 'scikit-learn' };
        const toLoad = [];
        for (const imp of imports) {
          const m = imp.match(/(?:import|from)\s+(\w+)/);
          if (m && pkgMap[m[1]]) {
            try {
              pyodide.runPython(`import ${m[1]}`);
            } catch {
              toLoad.push(pkgMap[m[1]]);
            }
            // Reset stderr after test import
            pyodide.runPython(`sys.stderr = io.StringIO()`);
          }
        }
        if (toLoad.length > 0) {
          outputDiv.innerHTML = `<span class="output-label">📦 Paketler yükleniyor: ${toLoad.join(', ')}...</span>`;
          outputDiv.classList.add('visible');
          await pyodide.loadPackage(toLoad);
          // Reset stdout/stderr after package loading
          pyodide.runPython(`
sys.stdout = io.StringIO()
sys.stderr = io.StringIO()
          `);
        }
      }

      pyodide.runPython(raw);
      const stdout = pyodide.runPython('sys.stdout.getvalue()');
      const stderr = pyodide.runPython('sys.stderr.getvalue()');

      let output = '';
      if (stdout) output += stdout;
      if (stderr) output += `<span class="output-error">${stderr}</span>`;
      if (!stdout && !stderr) output = '(Çıktı yok)';

      outputDiv.innerHTML = `<span class="output-label">📤 Çıktı</span>${escapeHtml(output)}`;
    } catch (pyErr) {
      outputDiv.innerHTML = `<span class="output-label">❌ Hata</span><span class="output-error">${escapeHtml(pyErr.message)}</span>`;
    }

    // Reset stdout
    pyodide.runPython(`
sys.stdout = sys.__stdout__
sys.stderr = sys.__stderr__
    `);
  } catch (e) {
    outputDiv.innerHTML = `<span class="output-label">❌ Hata</span><span class="output-error">${escapeHtml(e.message)}</span>`;
  }

  outputDiv.classList.add('visible');
  btn.innerHTML = '▶️ Çalıştır';
  btn.disabled = false;
}

function escapeHtml(s) {
  return s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
}

// ─── Table of Contents (Sidebar) ───
function buildTOC() {
  const nav = document.querySelector('.sidebar nav');
  if (!nav) return;

  const headings = document.querySelectorAll('.content h2, .content h3, .content h4');
  headings.forEach((h, i) => {
    if (!h.id) h.id = 'section-' + i;
    const a = document.createElement('a');
    a.href = '#' + h.id;
    a.textContent = h.textContent;
    a.className = 'toc-' + h.tagName.toLowerCase();
    nav.appendChild(a);
  });

  // Active state on scroll
  const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        nav.querySelectorAll('a').forEach(a => a.classList.remove('active'));
        const active = nav.querySelector(`a[href="#${entry.target.id}"]`);
        if (active) active.classList.add('active');
      }
    });
  }, { rootMargin: '-80px 0px -60% 0px', threshold: 0.1 });

  headings.forEach(h => observer.observe(h));
}

// ─── Scroll to Top ───
function initScrollTop() {
  const btn = document.querySelector('.scroll-top');
  if (!btn) return;
  window.addEventListener('scroll', () => {
    btn.classList.toggle('visible', window.scrollY > 400);
  });
  btn.addEventListener('click', () => window.scrollTo({ top: 0, behavior: 'smooth' }));
}

// ─── Mermaid Init ───
function initMermaid() {
  if (window.mermaid) {
    const isDark = document.documentElement.getAttribute('data-theme') === 'dark';
    mermaid.initialize({
      startOnLoad: true,
      theme: isDark ? 'dark' : 'default',
      securityLevel: 'loose',
      fontFamily: 'Inter, sans-serif',
    });
  }
}

// ─── Initialize Everything ───
document.addEventListener('DOMContentLoaded', () => {
  initTheme();
  buildCodeBlocks();
  buildTOC();
  initScrollTop();
  initMermaid();

  // Start loading Pyodide in background
  const hasPython = document.querySelector('.code-block[data-lang="python"]');
  if (hasPython) {
    setTimeout(() => loadPyodide_(), 2000);
  }
});
