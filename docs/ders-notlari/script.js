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
function getBlockRawCode(block) {
  const editor = block.querySelector('.code-editor');
  if (editor) return editor.value;
  return block.dataset.raw || '';
}

function syncBlockRaw(block) {
  const editor = block.querySelector('.code-editor');
  if (editor) {
    block.dataset.raw = editor.value;
    block.classList.toggle('code-modified', editor.value !== block.dataset.original);
  }
}

function isEditableBlock(block, lang) {
  if (block.dataset.readonly === 'true') return false;
  if (block.dataset.editable === 'false') return false;
  return lang === 'python' || lang === 'py';
}

const CODE_LANG_MAP = {
  'python': 'python', 'py': 'python',
  'json': 'json',
  'sql': 'sql',
  'bash': 'bash', 'shell': 'bash', 'sh': 'bash',
  'csv': 'plaintext', 'text': 'plaintext'
};

function getHljsLang(block) {
  const lang = (block.dataset.lang || 'text').toLowerCase();
  return CODE_LANG_MAP[lang] || 'plaintext';
}

function highlightEditorCode(block) {
  const editor = block.querySelector('.code-editor');
  const codeEl = block.querySelector('.code-editor-highlight code');
  if (!editor || !codeEl) return;

  const source = editor.value;
  const hljsLang = getHljsLang(block);

  if (window.hljs && hljsLang !== 'plaintext') {
    try {
      let html = hljs.highlight(source, { language: hljsLang }).value;
      if (source.endsWith('\n')) html += '\n';
      codeEl.innerHTML = html;
      return;
    } catch (e) {
      /* fall through to plain text */
    }
  }

  codeEl.textContent = source;
}

function syncEditorScroll(block) {
  const editor = block.querySelector('.code-editor');
  const gutter = block.querySelector('.code-line-gutter');
  const highlight = block.querySelector('.code-editor-highlight');
  if (!editor) return;

  if (gutter) gutter.scrollTop = editor.scrollTop;
  if (highlight) {
    highlight.scrollTop = editor.scrollTop;
    highlight.scrollLeft = editor.scrollLeft;
  }
}

function countEditorLines(text) {
  if (!text) return 1;
  return text.split('\n').length;
}

function updateCodeEditorLayout(block) {
  const editor = block.querySelector('.code-editor');
  const gutter = block.querySelector('.code-line-gutter');
  const highlight = block.querySelector('.code-editor-highlight');
  if (!editor || !gutter) return;

  const lineCount = countEditorLines(editor.value);
  gutter.textContent = Array.from({ length: lineCount }, (_, i) => i + 1).join('\n');

  editor.style.height = '0';
  editor.style.height = `${editor.scrollHeight}px`;
  gutter.style.minHeight = `${editor.scrollHeight}px`;
  if (highlight) highlight.style.minHeight = `${editor.scrollHeight}px`;
}

function setupCodeEditor(block, raw) {
  const pre = block.querySelector('pre');
  if (!pre) return;

  block.dataset.original = raw;
  block.dataset.raw = raw;
  block.classList.add('code-editable');

  const shell = document.createElement('div');
  shell.className = 'code-editor-shell';

  const gutter = document.createElement('div');
  gutter.className = 'code-line-gutter';
  gutter.setAttribute('aria-hidden', 'true');

  const area = document.createElement('div');
  area.className = 'code-editor-area';

  const highlightPre = document.createElement('pre');
  highlightPre.className = 'code-editor-highlight';
  highlightPre.setAttribute('aria-hidden', 'true');
  const highlightCode = document.createElement('code');
  highlightCode.className = `language-${getHljsLang(block)}`;
  highlightPre.appendChild(highlightCode);

  const editor = document.createElement('textarea');
  editor.className = 'code-editor';
  editor.spellcheck = false;
  editor.autocomplete = 'off';
  editor.autocapitalize = 'off';
  editor.value = raw;
  editor.setAttribute('aria-label', 'Düzenlenebilir kod editörü');
  editor.rows = 1;

  const onEditorChange = () => {
    syncBlockRaw(block);
    highlightEditorCode(block);
    updateCodeEditorLayout(block);
  };

  editor.addEventListener('input', onEditorChange);
  editor.addEventListener('scroll', () => syncEditorScroll(block));

  editor.addEventListener('keydown', (e) => {
    if (e.key === 'Tab') {
      e.preventDefault();
      const start = editor.selectionStart;
      const end = editor.selectionEnd;
      editor.value = editor.value.substring(0, start) + '  ' + editor.value.substring(end);
      editor.selectionStart = editor.selectionEnd = start + 2;
      onEditorChange();
    }
    if (e.key === 'Enter' && (e.ctrlKey || e.metaKey)) {
      e.preventDefault();
      block.querySelector('.run-btn')?.click();
    }
  });

  area.appendChild(highlightPre);
  area.appendChild(editor);
  shell.appendChild(gutter);
  shell.appendChild(area);

  pre.classList.add('code-editor-fallback');
  pre.hidden = true;
  pre.insertAdjacentElement('afterend', shell);

  highlightEditorCode(block);
  requestAnimationFrame(() => updateCodeEditorLayout(block));
}

function buildCodeBlocks() {
  document.querySelectorAll('.code-block').forEach(block => {
    const pre = block.querySelector('pre');
    const codeEl = pre?.querySelector('code');
    if (!codeEl) return;

    const lang = block.dataset.lang || 'text';
    const raw = codeEl.textContent;

    const editable = isEditableBlock(block, lang);

    if (editable) {
      setupCodeEditor(block, raw);
    } else {
      // Store raw code first
      block.dataset.raw = raw;
      block.dataset.original = raw;

      // Apply highlight.js
      const hljsLang = CODE_LANG_MAP[lang.toLowerCase()] || 'plaintext';
      codeEl.className = `language-${hljsLang}`;
      if (window.hljs) {
        hljs.highlightElement(codeEl);
      }

      // Add line numbers by wrapping each line
      const highlighted = codeEl.innerHTML;
      const lines = highlighted.split('\n');
      if (lines.length > 0 && lines[lines.length - 1].trim() === '') lines.pop();
      const wrappedLines = lines.map(line =>
        `<span class="line">${line || '\u00A0'}</span>`
      ).join('\n');
      codeEl.innerHTML = wrappedLines;
      pre.classList.add('line-numbers');
    }

    // Build header
    const header = block.querySelector('.code-header');
    if (!header) {
      const filename = block.dataset.filename || '';
      const canRun = (lang === 'python' || lang === 'py') && editable;
      const h = document.createElement('div');
      h.className = 'code-header';
      h.innerHTML = `
        <div class="code-header-left">
          ${filename ? `<span class="code-filename" title="Kaynak dosya">${filename}</span>` : ''}
          <span class="code-lang lang-${lang}">${lang}</span>
          ${editable ? '<span class="code-editable-badge" title="Kodu düzenleyebilirsiniz">✏️ düzenlenebilir</span>' : ''}
        </div>
        <div class="code-actions">
          ${editable ? '<button onclick="resetCode(this)" title="Varsayılan koda dön" class="reset-btn">↩️ Sıfırla</button>' : ''}
          <button onclick="copyCode(this)" title="Kopyala">📋 Kopyala</button>
          ${canRun ? `<button onclick="runCode(this)" title="Çalıştır (Ctrl+Enter)" class="run-btn">▶️ Çalıştır</button>` : ''}
        </div>
      `;
      block.insertBefore(h, pre);
    }
  });
}

// ─── KaTeX (math formulas) ───
function initMath() {
  if (!window.renderMathInElement) return;
  renderMathInElement(document.querySelector('.content') || document.body, {
    delimiters: [
      { left: '\\[', right: '\\]', display: true },
      { left: '\\(', right: '\\)', display: false },
    ],
    throwOnError: false,
    ignoredTags: ['script', 'noscript', 'style', 'textarea', 'pre', 'code'],
  });
}

function scheduleMath() {
  if (window.renderMathInElement) initMath();
  else window.addEventListener('load', initMath, { once: true });
}

// ─── Copy Code ───
function copyCode(btn) {
  const block = btn.closest('.code-block');
  syncBlockRaw(block);
  const raw = getBlockRawCode(block);
  navigator.clipboard.writeText(raw).then(() => {
    btn.classList.add('copied');
    btn.innerHTML = '✅ Kopyalandı!';
    setTimeout(() => {
      btn.classList.remove('copied');
      btn.innerHTML = '📋 Kopyala';
    }, 2000);
  });
}

// ─── Reset Code to Original ───
function resetCode(btn) {
  const block = btn.closest('.code-block');
  const editor = block.querySelector('.code-editor');
  if (!editor) return;

  editor.value = block.dataset.original;
  syncBlockRaw(block);
  highlightEditorCode(block);
  updateCodeEditorLayout(block);
  editor.focus();

  btn.classList.add('copied');
  const prev = btn.innerHTML;
  btn.innerHTML = '✅ Sıfırlandı';
  setTimeout(() => {
    btn.classList.remove('copied');
    btn.innerHTML = prev;
  }, 1500);
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
  syncBlockRaw(block);
  const raw = getBlockRawCode(block);

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
      fontSize: 16,
      flowchart: {
        useMaxWidth: true,
        htmlLabels: true,
        curve: 'basis',
        nodeSpacing: 60,
        rankSpacing: 70,
        padding: 20,
      },
      gantt: {
        useMaxWidth: true,
        fontSize: 14,
        barHeight: 24,
        barGap: 6,
      },
      themeVariables: {
        fontSize: '16px',
      },
    });
  }
}

// ─── Initialize Everything ───
document.addEventListener('DOMContentLoaded', () => {
  initTheme();
  buildCodeBlocks();
  scheduleMath();
  buildTOC();
  initScrollTop();
  initMermaid();

  window.addEventListener('load', () => {
    document.querySelectorAll('.code-editable').forEach(block => {
      highlightEditorCode(block);
      updateCodeEditorLayout(block);
    });
  });

  // Start loading Pyodide in background
  const hasPython = document.querySelector('.code-block[data-lang="python"]');
  const preloadNumpy = document.body.dataset.preloadNumpy === 'true'
    || document.querySelector('.handbook-content');
  if (preloadNumpy && hasPython) {
    setTimeout(async () => {
      const pyodide = await loadPyodide_();
      if (pyodide) {
        try {
          await pyodide.loadPackage(['numpy']);
          updatePyodideStatus('NumPy hazır ✓');
          document.querySelector('.pyodide-status')?.classList.add('ready');
        } catch (e) {
          console.warn('NumPy ön yükleme:', e);
        }
      }
    }, 800);
  } else if (hasPython) {
    setTimeout(() => loadPyodide_(), 2000);
  }
});
