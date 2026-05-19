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
let pyodidePackagesLoaded = new Set();
let matplotlibBootstrapped = false;
let seabornBootstrapped = false;
let sklearnBootstrapped = false;
let pyodideHttpPatched = false;

function codeNeedsNetworking(raw) {
  return /load_dataset|fetch_openml|fetch_california|fetch_lfw|fetch_mldata|urllib\.request|requests\.(?:get|post)/.test(raw);
}

function codeNeedsSklearn(raw) {
  return /(?:^|\n)\s*(?:import|from)\s+sklearn|sklearn\.|\bGridSearchCV\b|\bcross_val_score\b|\btrain_test_split\b|\bPipeline\b|\bStandardScaler\b|\bKMeans\b|\bPCA\b|\bSVC\b|\bRandomForest|\bGaussianNB\b|\bLinearRegression\b|\bmake_classification\b|\bmake_blobs\b/.test(raw);
}

function codeNeedsMatplotlib(raw) {
  return /(?:^|\n)\s*(?:import|from)\s+matplotlib|matplotlib\.|pyplot|\bplt\.|(?:^|\n)\s*(?:import|from)\s+seaborn|\bsns\./.test(raw);
}

function codeNeedsNumpy(raw) {
  return codeNeedsMatplotlib(raw)
    || codeNeedsSklearn(raw)
    || /(?:^|\n)\s*(?:import|from)\s+numpy|\bnp\./.test(raw);
}

function codeNeedsPandas(raw) {
  return codeNeedsSklearn(raw)
    || /(?:^|\n)\s*(?:import|from)\s+pandas|\bpd\.|(?:^|\n)\s*(?:import|from)\s+seaborn|\bsns\./.test(raw);
}

function codeNeedsSeaborn(raw) {
  return /(?:^|\n)\s*(?:import|from)\s+seaborn|\bsns\./.test(raw);
}

function pagePreloadsMatplotlib() {
  return document.body.dataset.preloadMatplotlib === 'true';
}

function pagePreloadsSeaborn() {
  return document.body.dataset.preloadSeaborn === 'true';
}

function pagePreloadsSklearn() {
  return document.body.dataset.preloadSklearn === 'true';
}

async function loadPyodidePackages(pyodide, packages, statusHost) {
  const pending = packages.filter(p => !pyodidePackagesLoaded.has(p));
  if (!pending.length) return;
  if (statusHost) {
    statusHost.innerHTML = `<span class="output-label">📦 Paketler yükleniyor: ${pending.join(', ')}...</span>`;
    statusHost.closest('.run-output')?.classList.add('visible');
  }
  await pyodide.loadPackage(pending);
  pending.forEach(p => pyodidePackagesLoaded.add(p));
}

/** Pyodide stdlib urllib does not speak https; patch via pyodide-http (Seaborn load_dataset, sklearn fetch_*). */
async function enablePyodideNetworking(pyodide, statusHost) {
  if (pyodideHttpPatched) return;
  await loadPyodidePackages(pyodide, ['micropip'], statusHost);
  try {
    await loadPyodidePackages(pyodide, ['ssl'], statusHost);
  } catch (e) {
    console.warn('ssl paketi yüklenemedi (isteğe bağlı):', e);
  }
  if (statusHost) {
    statusHost.innerHTML = '<span class="output-label">🌐 HTTPS ağı etkinleştiriliyor (pyodide-http)...</span>';
    statusHost.closest('.run-output')?.classList.add('visible');
  }
  await pyodide.runPythonAsync(`
import micropip
await micropip.install("pyodide-http")
import pyodide_http
pyodide_http.patch_all()
`);
  pyodideHttpPatched = true;
}

async function loadSeabornPackage(pyodide, statusHost) {
  if (pyodidePackagesLoaded.has('seaborn')) return;

  await loadPyodidePackages(pyodide, ['numpy', 'pandas', 'matplotlib', 'micropip'], statusHost);
  try {
    await loadPyodidePackages(pyodide, ['scipy'], statusHost);
  } catch (e) {
    console.warn('SciPy (Seaborn için isteğe bağlı) yüklenemedi:', e);
  }

  await enablePyodideNetworking(pyodide, statusHost);

  const statusText = '📦 Seaborn yükleniyor (micropip/PyPI — ilk seferde 30–60 sn sürebilir)...';
  if (statusHost) {
    statusHost.innerHTML = `<span class="output-label">${statusText}</span>`;
    statusHost.closest('.run-output')?.classList.add('visible');
  } else {
    updatePyodideStatus(statusText);
  }

  await pyodide.runPythonAsync(`
import micropip
await micropip.install("seaborn")
import seaborn as sns
`);
  pyodidePackagesLoaded.add('seaborn');
}

async function bootstrapSeabornSession(pyodide, statusHost) {
  await loadSeabornPackage(pyodide, statusHost);
  await bootstrapMatplotlibSession(pyodide, statusHost);
  if (seabornBootstrapped) return;
  pyodide.runPython(`
import seaborn as sns
import pandas as pd
try:
    sns.set()
except Exception:
    pass
`);
  seabornBootstrapped = true;
}

async function loadSklearnPackage(pyodide, statusHost) {
  if (pyodidePackagesLoaded.has('scikit-learn')) return;

  const statusText = '📦 scikit-learn yükleniyor (ilk seferde 30–90 sn sürebilir)...';
  if (statusHost) {
    statusHost.innerHTML = `<span class="output-label">${statusText}</span>`;
    statusHost.closest('.run-output')?.classList.add('visible');
  } else {
    updatePyodideStatus(statusText);
  }

  await loadPyodidePackages(pyodide, ['scikit-learn'], statusHost);
  await enablePyodideNetworking(pyodide, statusHost);
}

async function bootstrapSklearnSession(pyodide, statusHost) {
  await loadSklearnPackage(pyodide, statusHost);
  await bootstrapMatplotlibSession(pyodide, statusHost);
  if (sklearnBootstrapped) return;
  pyodide.runPython(`
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn
plt.close('all')
`);
  sklearnBootstrapped = true;
}

async function ensurePackagesForCode(pyodide, raw, statusHost) {
  const needsSk = codeNeedsSklearn(raw) || pagePreloadsSklearn();
  const needsSb = codeNeedsSeaborn(raw) || pagePreloadsSeaborn();
  const needsNp = codeNeedsNumpy(raw) || pagePreloadsMatplotlib() || pagePreloadsSeaborn() || pagePreloadsSklearn();
  const needsMpl = codeNeedsMatplotlib(raw) || pagePreloadsMatplotlib() || pagePreloadsSeaborn() || pagePreloadsSklearn();
  const needsPd = codeNeedsPandas(raw) || pagePreloadsSeaborn() || pagePreloadsSklearn();

  const toLoad = [];
  if (needsNp) toLoad.push('numpy');
  if (needsPd) toLoad.push('pandas');
  if (needsMpl) toLoad.push('matplotlib');
  if (needsSk) toLoad.push('scipy');
  await loadPyodidePackages(pyodide, toLoad, statusHost);

  if (needsSk) await loadSklearnPackage(pyodide, statusHost);
  if (needsSb) await loadSeabornPackage(pyodide, statusHost);
  if (!needsSk && !needsSb && (codeNeedsNetworking(raw) || pagePreloadsSeaborn())) {
    await enablePyodideNetworking(pyodide, statusHost);
  }
}

async function bootstrapMatplotlibSession(pyodide, statusHost) {
  await ensurePackagesForCode(pyodide, 'import matplotlib.pyplot as plt\nimport numpy as np', statusHost);
  if (matplotlibBootstrapped) return;
  pyodide.runPython(`
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
plt.close('all')
for _style in ('seaborn-v0_8-whitegrid', 'seaborn-whitegrid', 'classic'):
    try:
        plt.style.use(_style)
        break
    except Exception:
        pass
`);
  matplotlibBootstrapped = true;
}

function resetRunOutput(block) {
  let outputDiv = block.querySelector('.run-output');
  if (!outputDiv) {
    outputDiv = document.createElement('div');
    outputDiv.className = 'run-output';
    block.appendChild(outputDiv);
  }
  outputDiv.replaceChildren();
  const textHost = document.createElement('div');
  textHost.className = 'run-output-text';
  const mplHost = document.createElement('div');
  mplHost.className = 'mpl-target';
  outputDiv.appendChild(textHost);
  outputDiv.appendChild(mplHost);
  outputDiv.classList.remove('visible');
  return { outputDiv, textHost, mplHost };
}

function setMplRenderTarget(mplHost) {
  mplHost.replaceChildren();
  document.pyodideMplTarget = mplHost;
}

function clearMplRenderTarget() {
  document.pyodideMplTarget = undefined;
}

function shouldManageFigures(raw, runnable) {
  return codeNeedsMatplotlib(raw)
    || codeNeedsMatplotlib(runnable)
    || codeNeedsSeaborn(raw)
    || codeNeedsSeaborn(runnable)
    || (pagePreloadsSklearn() && /\bplt\.|\bax\.|\.plot\(|\.scatter\(|\.figure\(/.test(runnable))
    || (pagePreloadsMatplotlib() && /\bplt\.|\bax\.|\bsns\.|\.plot\(|\.scatter\(|\.figure\(/.test(runnable))
    || (pagePreloadsSeaborn() && /\bsns\.|seaborn/.test(runnable));
}

function stripMagicLines(raw) {
  return raw.split('\n').filter(line => !/^\s*%/.test(line)).join('\n').trim();
}

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
  const runnable = stripMagicLines(raw);

  btn.innerHTML = '⏳ Çalışıyor...';
  btn.disabled = true;

  const { outputDiv, textHost, mplHost } = resetRunOutput(block);

  try {
    const pyodide = await loadPyodide_();
    if (!pyodide) {
      textHost.innerHTML = '<span class="output-label">Hata</span><span class="output-error">Pyodide yüklenemedi. Sayfayı yenileyin.</span>';
      outputDiv.classList.add('visible');
      return;
    }

    const usesMpl = shouldManageFigures(raw, runnable);
    const usesNp = codeNeedsNumpy(raw) || codeNeedsNumpy(runnable) || usesMpl;

    try {
      await ensurePackagesForCode(pyodide, raw + '\n' + runnable, textHost);

      if (codeNeedsSeaborn(raw) || codeNeedsSeaborn(runnable) || pagePreloadsSeaborn()) {
        await bootstrapSeabornSession(pyodide, textHost);
      } else if (codeNeedsSklearn(raw) || codeNeedsSklearn(runnable) || pagePreloadsSklearn()) {
        await bootstrapSklearnSession(pyodide, textHost);
      } else if (usesMpl || (pagePreloadsMatplotlib() && usesNp)) {
        await bootstrapMatplotlibSession(pyodide, textHost);
      }

      // Önceki hücrelerden kalan şekiller bu bloğa karışmasın
      if (matplotlibBootstrapped || seabornBootstrapped || sklearnBootstrapped || usesMpl) {
        pyodide.runPython(`
import matplotlib.pyplot as plt
plt.close('all')
        `);
      }

      setMplRenderTarget(mplHost);

      pyodide.runPython(`
import sys, io
sys.stdout = io.StringIO()
sys.stderr = io.StringIO()
      `);

      if (runnable) {
        pyodide.runPython(runnable);
      }

      if (matplotlibBootstrapped || seabornBootstrapped || sklearnBootstrapped || usesMpl) {
        pyodide.runPython(`
import matplotlib.pyplot as plt
_has_data = False
for _n in plt.get_fignums():
    _fig = plt.figure(_n)
    for _ax in _fig.axes:
        if _ax.has_data():
            _has_data = True
            break
if _has_data:
    plt.show()
plt.close('all')
        `);
      }

      const stdout = pyodide.runPython('sys.stdout.getvalue()');
      const stderr = pyodide.runPython('sys.stderr.getvalue()');

      const hasPlot = mplHost.children.length > 0;
      const parts = [];
      if (hasPlot) parts.push('<span class="output-label">📊 Grafik</span>');
      if (stdout.trim()) {
        parts.push(`<span class="output-label">${hasPlot ? '📤 Metin' : '📤 Çıktı'}</span>${escapeHtml(stdout)}`);
      }
      if (stderr.trim()) {
        parts.push(`<span class="output-error">${escapeHtml(stderr)}</span>`);
      }
      if (!parts.length) {
        parts.push('<span class="output-label">📤 Çıktı</span>(Çıktı yok — üstteki hücreleri sırayla çalıştırın veya değişkenlerin tanımlı olduğundan emin olun)');
      }
      textHost.innerHTML = parts.join('');
    } catch (pyErr) {
      let errHtml = escapeHtml(pyErr.message);
      if (/No module named|module not found/i.test(pyErr.message)) {
        errHtml += '<br><span class="output-hint">💡 Gerekli paket yüklenemedi. Sayfayı yenileyip sol alttaki durum çubuğunda paketlerin hazır olmasını bekleyin.</span>';
      } else if (/unknown url type:\s*https|URLError|urlopen error/i.test(pyErr.message)) {
        errHtml += '<br><span class="output-hint">💡 HTTPS ağı etkinleştirilemedi. Sayfayı yenileyip tekrar deneyin; hâlâ olmazsa veri setini Jupyter .ipynb ile indirip çalıştırın.</span>';
      } else if (/sklearn|scikit-learn/i.test(pyErr.message)) {
        errHtml += '<br><span class="output-hint">💡 scikit-learn Pyodide\'da büyük bir pakettir — sol altta “scikit-learn hazır ✓” görünene kadar bekleyin. Bazı örnekler internet gerektirir (<code>fetch_openml</code>). Tam deneyim için .ipynb + Jupyter önerilir.</span>';
      } else if (/seaborn|sns/i.test(pyErr.message)) {
        errHtml += '<br><span class="output-hint">💡 Seaborn Pyodide\'da micropip ile yüklenir — ilk seferde uzun sürebilir. <code>sns.load_dataset</code> internet gerektirir; <code>lmplot</code>/<code>regplot</code> statsmodels isteyebilir. Tam deneyim için .ipynb + Jupyter önerilir.</span>';
      } else if (/NameError|is not defined|not defined/i.test(pyErr.message)) {
        errHtml += '<br><span class="output-hint">💡 Bu blok üstteki kodlara bağımlı olabilir — yukarıdaki Python bloklarını sırayla çalıştırın veya 📥 notebook indirip Jupyter\'de deneyin.</span>';
      } else if (/matplotlib|pyplot|plt/i.test(pyErr.message)) {
        errHtml += '<br><span class="output-hint">💡 Matplotlib tarayıcıda sınırlıdır; tam grafik için .ipynb dosyasını Jupyter\'de açın.</span>';
      }
      textHost.innerHTML = `<span class="output-label">❌ Hata</span><span class="output-error">${errHtml}</span>`;
      mplHost.replaceChildren();
    } finally {
      clearMplRenderTarget();
    }

    pyodide.runPython(`
sys.stdout = sys.__stdout__
sys.stderr = sys.__stderr__
    `);
  } catch (e) {
    textHost.innerHTML = `<span class="output-label">❌ Hata</span><span class="output-error">${escapeHtml(e.message)}</span>`;
    mplHost.replaceChildren();
    clearMplRenderTarget();
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

  const headings = document.querySelectorAll('.content h1, .content h2, .content h3, .content h4');
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
    || document.body.dataset.preloadPandas === 'true'
    || document.body.dataset.preloadMatplotlib === 'true'
    || document.body.dataset.preloadSklearn === 'true'
    || document.querySelector('.handbook-content');
  const preloadPandas = document.body.dataset.preloadPandas === 'true';
  const preloadMatplotlib = document.body.dataset.preloadMatplotlib === 'true';
  const preloadSeaborn = document.body.dataset.preloadSeaborn === 'true';
  const preloadSklearn = document.body.dataset.preloadSklearn === 'true';
  if ((preloadNumpy || preloadPandas || preloadMatplotlib || preloadSeaborn || preloadSklearn) && hasPython) {
    setTimeout(async () => {
      const pyodide = await loadPyodide_();
      if (pyodide) {
        try {
          const pkgs = [];
          if (preloadNumpy || preloadPandas || preloadMatplotlib || preloadSeaborn || preloadSklearn) pkgs.push('numpy');
          if (preloadPandas || preloadSeaborn || preloadSklearn) pkgs.push('pandas');
          if (preloadMatplotlib || preloadSeaborn || preloadSklearn) pkgs.push('matplotlib');
          if (preloadSklearn) pkgs.push('scipy');
          await loadPyodidePackages(pyodide, pkgs, null);
          if (preloadSeaborn) {
            await bootstrapSeabornSession(pyodide, null);
          } else if (preloadSklearn) {
            await bootstrapSklearnSession(pyodide, null);
          } else if (preloadMatplotlib) {
            await bootstrapMatplotlibSession(pyodide, null);
          }
          let label = 'NumPy hazır ✓';
          if (preloadSeaborn) label = 'NumPy + Pandas + Matplotlib + Seaborn hazır ✓';
          else if (preloadSklearn) label = 'NumPy + Pandas + Matplotlib + scikit-learn hazır ✓';
          else if (preloadMatplotlib) label = 'NumPy + Matplotlib hazır ✓';
          else if (preloadPandas) label = 'NumPy + Pandas hazır ✓';
          updatePyodideStatus(label);
          document.querySelector('.pyodide-status')?.classList.add('ready');
        } catch (e) {
          console.warn('Paket ön yükleme:', e);
          const msg = preloadSeaborn
            ? 'Seaborn yüklenemedi — internet bağlantısı gerekir'
            : preloadSklearn
              ? 'scikit-learn yüklenemedi — sayfayı yenileyin'
              : 'Paket yükleme hatası — sayfayı yenileyin';
          updatePyodideStatus(msg);
        }
      }
    }, 800);
  } else if (hasPython) {
    setTimeout(() => loadPyodide_(), 2000);
  }
});
