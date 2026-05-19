/* PDS Handbook — chapter navigation (standalone-friendly) */
window.HANDBOOK_NAV = {
  courseNotesUrl: '../ders-notlari/hafta1.html',
  chapters: [
    {
      id: '01-ipython',
      title: 'Bölüm 1 — IPython',
      icon: '⚡',
      index: 'chapters/01-ipython/index.html',
      sections: [
        { slug: '00-introduction', title: 'IPython\'a Giriş', source: '01.00-ipython-beyond-normal-python.html', notebook: '01-ipython/00-introduction.ipynb' },
        { slug: '01-help-and-documentation', title: '1.1 Yardım ve Dokümantasyon', source: '01.01-help-and-documentation.html', notebook: '01-ipython/01-help-and-documentation.ipynb' },
        { slug: '02-keyboard-shortcuts', title: '1.2 Klavye Kısayolları', source: '01.02-shell-keyboard-shortcuts.html', notebook: '01-ipython/02-keyboard-shortcuts.ipynb' },
        { slug: '03-magic-commands', title: '1.3 Magic Komutlar', source: '01.03-magic-commands.html', notebook: '01-ipython/03-magic-commands.ipynb' },
        { slug: '04-input-output-history', title: '1.4 Girdi ve Çıktı Geçmişi', source: '01.04-input-output-history.html', notebook: '01-ipython/04-input-output-history.ipynb' },
        { slug: '05-shell-commands', title: '1.5 IPython ve Shell', source: '01.05-ipython-and-shell-commands.html', notebook: '01-ipython/05-shell-commands.ipynb' },
        { slug: '06-errors-and-debugging', title: '1.6 Hatalar ve Hata Ayıklama', source: '01.06-errors-and-debugging.html', notebook: '01-ipython/06-errors-and-debugging.ipynb' },
        { slug: '07-timing-and-profiling', title: '1.7 Profil ve Zamanlama', source: '01.07-timing-and-profiling.html', notebook: '01-ipython/07-timing-and-profiling.ipynb' },
        { slug: '08-more-resources', title: '1.8 Daha Fazla Kaynak', source: '01.08-more-ipython-resources.html', notebook: '01-ipython/08-more-resources.ipynb' },
      ],
    },
    {
      id: '02-numpy',
      title: 'Bölüm 2 — NumPy',
      icon: '🐍',
      index: 'chapters/02-numpy/index.html',
      preloadNumpy: true,
      sections: [
        { slug: '00-introduction', title: 'NumPy\'ye Giriş', source: '02.00-introduction-to-numpy.html', notebook: '02-numpy/00-introduction.ipynb' },
        { slug: '01-understanding-data-types', title: '2.1 Veri Tipleri', source: '02.01-understanding-data-types.html', notebook: '02-numpy/01-understanding-data-types.ipynb' },
        { slug: '02-basics-of-numpy-arrays', title: '2.2 Dizi Temelleri', source: '02.02-the-basics-of-numpy-arrays.html', notebook: '02-numpy/02-basics-of-numpy-arrays.ipynb' },
        { slug: '03-computation-ufuncs', title: '2.3 UFuncs', source: '02.03-computation-on-arrays-ufuncs.html', notebook: '02-numpy/03-computation-ufuncs.ipynb' },
        { slug: '04-aggregates', title: '2.4 Agregasyonlar', source: '02.04-computation-on-arrays-aggregates.html', notebook: '02-numpy/04-aggregates.ipynb' },
        { slug: '05-broadcasting', title: '2.5 Broadcasting', source: '02.05-computation-on-arrays-broadcasting.html', notebook: '02-numpy/05-broadcasting.ipynb' },
        { slug: '06-boolean-masks', title: '2.6 Boolean Maskeler', source: '02.06-boolean-arrays-and-masks.html', notebook: '02-numpy/06-boolean-masks.ipynb' },
        { slug: '07-fancy-indexing', title: '2.7 Fancy Indexing', source: '02.07-fancy-indexing.html', notebook: '02-numpy/07-fancy-indexing.ipynb' },
        { slug: '08-sorting', title: '2.8 Sıralama', source: '02.08-sorting.html', notebook: '02-numpy/08-sorting.ipynb' },
        { slug: '09-structured-arrays', title: '2.9 Yapılandırılmış Diziler', source: '02.09-structured-data-numpy.html', notebook: '02-numpy/09-structured-arrays.ipynb' },
      ],
    },
    {
      id: '03-pandas',
      title: 'Bölüm 3 — Pandas',
      icon: '🐼',
      index: 'chapters/03-pandas/index.html',
      preloadNumpy: true,
      preloadPandas: true,
      sections: [
        { slug: '00-introduction', title: 'Pandas\'a Giriş', source: '03.00-introduction-to-pandas.html', notebook: '03-pandas/00-introduction.ipynb' },
        { slug: '01-introducing-pandas-objects', title: '3.1 Pandas Nesneleri', source: '03.01-introducing-pandas-objects.html', notebook: '03-pandas/01-introducing-pandas-objects.ipynb' },
        { slug: '02-data-indexing-and-selection', title: '3.2 İndeksleme ve Seçim', source: '03.02-data-indexing-and-selection.html', notebook: '03-pandas/02-data-indexing-and-selection.ipynb' },
        { slug: '03-operations-in-pandas', title: '3.3 Pandas İşlemleri', source: '03.03-operations-in-pandas.html', notebook: '03-pandas/03-operations-in-pandas.ipynb' },
        { slug: '04-missing-values', title: '3.4 Eksik Veri', source: '03.04-missing-values.html', notebook: '03-pandas/04-missing-values.ipynb' },
        { slug: '05-hierarchical-indexing', title: '3.5 Hiyerarşik İndeks', source: '03.05-hierarchical-indexing.html', notebook: '03-pandas/05-hierarchical-indexing.ipynb' },
        { slug: '06-concat-and-append', title: '3.6 Concat ve Append', source: '03.06-concat-and-append.html', notebook: '03-pandas/06-concat-and-append.ipynb' },
        { slug: '07-merge-and-join', title: '3.7 Merge ve Join', source: '03.07-merge-and-join.html', notebook: '03-pandas/07-merge-and-join.ipynb' },
        { slug: '08-aggregation-and-grouping', title: '3.8 Agregasyon ve Gruplama', source: '03.08-aggregation-and-grouping.html', notebook: '03-pandas/08-aggregation-and-grouping.ipynb' },
        { slug: '09-pivot-tables', title: '3.9 Pivot Tablolar', source: '03.09-pivot-tables.html', notebook: '03-pandas/09-pivot-tables.ipynb' },
        { slug: '10-working-with-strings', title: '3.10 Dizeler', source: '03.10-working-with-strings.html', notebook: '03-pandas/10-working-with-strings.ipynb' },
        { slug: '11-working-with-time-series', title: '3.11 Zaman Serileri', source: '03.11-working-with-time-series.html', notebook: '03-pandas/11-working-with-time-series.ipynb' },
        { slug: '12-performance-eval-and-query', title: '3.12 Performans ve Sorgu', source: '03.12-performance-eval-and-query.html', notebook: '03-pandas/12-performance-eval-and-query.ipynb' },
        { slug: '13-further-resources', title: '3.13 Kaynaklar', source: '03.13-further-pandas-resources.html', notebook: '03-pandas/13-further-resources.ipynb' },
      ],
    },
    {
      id: '04-matplotlib',
      title: 'Bölüm 4 — Matplotlib',
      icon: '📊',
      index: 'chapters/04-matplotlib/index.html',
      preloadNumpy: true,
      preloadMatplotlib: true,
      sections: [
        { slug: '00-introduction', title: 'Matplotlib\'e Giriş', source: '04.00-introduction-to-matplotlib.html', notebook: '04-matplotlib/00-introduction.ipynb' },
        { slug: '01-simple-line-plots', title: '4.1 Çizgi Grafikleri', source: '04.01-simple-line-plots.html', notebook: '04-matplotlib/01-simple-line-plots.ipynb' },
        { slug: '02-simple-scatter-plots', title: '4.2 Saçılım Grafikleri', source: '04.02-simple-scatter-plots.html', notebook: '04-matplotlib/02-simple-scatter-plots.ipynb' },
        { slug: '03-errorbars', title: '4.3 Hata Çubukları', source: '04.03-errorbars.html', notebook: '04-matplotlib/03-errorbars.ipynb' },
        { slug: '04-density-and-contour-plots', title: '4.4 Yoğunluk ve Kontur', source: '04.04-density-and-contour-plots.html', notebook: '04-matplotlib/04-density-and-contour-plots.ipynb' },
        { slug: '05-histograms-and-binnings', title: '4.5 Histogramlar', source: '04.05-histograms-and-binnings.html', notebook: '04-matplotlib/05-histograms-and-binnings.ipynb' },
        { slug: '06-customizing-legends', title: '4.6 Lejantlar', source: '04.06-customizing-legends.html', notebook: '04-matplotlib/06-customizing-legends.ipynb' },
        { slug: '07-customizing-colorbars', title: '4.7 Renk Çubukları', source: '04.07-customizing-colorbars.html', notebook: '04-matplotlib/07-customizing-colorbars.ipynb' },
        { slug: '08-multiple-subplots', title: '4.8 Alt Grafikler', source: '04.08-multiple-subplots.html', notebook: '04-matplotlib/08-multiple-subplots.ipynb' },
        { slug: '09-text-and-annotation', title: '4.9 Metin ve Açıklama', source: '04.09-text-and-annotation.html', notebook: '04-matplotlib/09-text-and-annotation.ipynb' },
        { slug: '10-customizing-ticks', title: '4.10 Eksen İşaretleri', source: '04.10-customizing-ticks.html', notebook: '04-matplotlib/10-customizing-ticks.ipynb' },
        { slug: '11-settings-and-stylesheets', title: '4.11 Ayarlar ve Stiller', source: '04.11-settings-and-stylesheets.html', notebook: '04-matplotlib/11-settings-and-stylesheets.ipynb' },
        { slug: '12-three-dimensional-plotting', title: '4.12 3B Çizim', source: '04.12-three-dimensional-plotting.html', notebook: '04-matplotlib/12-three-dimensional-plotting.ipynb' },
        { slug: '14-visualization-with-seaborn', title: '4.14 Seaborn', source: '04.14-visualization-with-seaborn.html', notebook: '04-matplotlib/14-visualization-with-seaborn.ipynb' },
        { slug: '15-further-resources', title: '4.15 Kaynaklar', source: '04.15-further-matplotlib-resources.html', notebook: '04-matplotlib/15-further-resources.ipynb' },
      ],
    },
    {
      id: '05-sklearn',
      title: 'Bölüm 5 — Makine Öğrenmesi',
      icon: '🤖',
      index: 'chapters/05-sklearn/index.html',
      preloadNumpy: true,
      preloadPandas: true,
      preloadMatplotlib: true,
      preloadSklearn: true,
      sections: [
        { slug: '00-introduction', title: 'Makine Öğrenmesine Giriş', source: '05.00-machine-learning.html', notebook: '05-sklearn/00-introduction.ipynb' },
        { slug: '01-what-is-machine-learning', title: '5.1 Makine Öğrenmesi Nedir?', source: '05.01-what-is-machine-learning.html', notebook: '05-sklearn/01-what-is-machine-learning.ipynb' },
        { slug: '02-introducing-scikit-learn', title: '5.2 Scikit-Learn', source: '05.02-introducing-scikit-learn.html', notebook: '05-sklearn/02-introducing-scikit-learn.ipynb' },
        { slug: '03-hyperparameters-and-model-validation', title: '5.3 Hiperparametreler', source: '05.03-hyperparameters-and-model-validation.html', notebook: '05-sklearn/03-hyperparameters-and-model-validation.ipynb' },
        { slug: '04-feature-engineering', title: '5.4 Öznitelik Mühendisliği', source: '05.04-feature-engineering.html', notebook: '05-sklearn/04-feature-engineering.ipynb' },
        { slug: '05-naive-bayes', title: '5.5 Naive Bayes', source: '05.05-naive-bayes.html', notebook: '05-sklearn/05-naive-bayes.ipynb' },
        { slug: '06-linear-regression', title: '5.6 Doğrusal Regresyon', source: '05.06-linear-regression.html', notebook: '05-sklearn/06-linear-regression.ipynb' },
        { slug: '07-support-vector-machines', title: '5.7 SVM', source: '05.07-support-vector-machines.html', notebook: '05-sklearn/07-support-vector-machines.ipynb' },
        { slug: '08-random-forests', title: '5.8 Rastgele Ormanlar', source: '05.08-random-forests.html', notebook: '05-sklearn/08-random-forests.ipynb' },
        { slug: '09-principal-component-analysis', title: '5.9 PCA', source: '05.09-principal-component-analysis.html', notebook: '05-sklearn/09-principal-component-analysis.ipynb' },
        { slug: '10-manifold-learning', title: '5.10 Manifold', source: '05.10-manifold-learning.html', notebook: '05-sklearn/10-manifold-learning.ipynb' },
        { slug: '11-k-means', title: '5.11 K-Means', source: '05.11-k-means.html', notebook: '05-sklearn/11-k-means.ipynb' },
        { slug: '12-gaussian-mixtures', title: '5.12 Gauss Karışımları', source: '05.12-gaussian-mixtures.html', notebook: '05-sklearn/12-gaussian-mixtures.ipynb' },
        { slug: '13-kernel-density-estimation', title: '5.13 KDE', source: '05.13-kernel-density-estimation.html', notebook: '05-sklearn/13-kernel-density-estimation.ipynb' },
        { slug: '14-image-features', title: '5.14 Görüntü Öznitelikleri', source: '05.14-image-features.html', notebook: '05-sklearn/14-image-features.ipynb' },
        { slug: '15-learning-more', title: '5.15 Kaynaklar', source: '05.15-learning-more.html', notebook: '05-sklearn/15-learning-more.ipynb' },
      ],
    },
  ],
};

function navEscapeHtml(s) {
  return String(s)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;');
}

function handbookBasePrefix() {
  const depth = parseInt(document.body.dataset.depth || '0', 10);
  return depth > 0 ? '../'.repeat(depth) : '';
}

function findSectionMeta(nav, chapterId, sectionSlug) {
  const ch = nav.chapters.find(c => c.id === chapterId);
  const sec = ch?.sections.find(s => s.slug === sectionSlug);
  return { ch, sec };
}

function initHandbookNav() {
  const body = document.body;
  if (!body.classList.contains('pds-handbook-site')) return;

  const prefix = handbookBasePrefix();
  const chapterId = body.dataset.chapter;
  const sectionSlug = body.dataset.section;
  const nav = window.HANDBOOK_NAV;
  if (!nav) return;

  const courseLink = document.querySelector('[data-handbook-course-link]');
  if (courseLink) {
    const depth = parseInt(body.dataset.depth || '0', 10);
    const coursePath = body.dataset.courseNotes || '../ders-notlari/hafta1.html';
    if (coursePath.startsWith('http')) {
      courseLink.href = coursePath;
    } else {
      const up = '../'.repeat(depth + 1);
      courseLink.href = coursePath.startsWith('../')
        ? up + coursePath.replace(/^\.\.\//, '')
        : prefix + coursePath;
    }
  }

  const brand = document.querySelector('.nav-brand');
  if (brand) brand.href = prefix + 'index.html';

  const backLink = document.querySelector('.handbook-back-link');
  if (backLink) backLink.href = prefix + 'index.html';

  const chapterList = document.querySelector('.handbook-chapter-list');
  if (chapterList) {
    chapterList.innerHTML = nav.chapters.map(ch => {
      const href = prefix + ch.index;
      const cls = ch.id === chapterId ? ' class="current-chapter"' : '';
      return `<a href="${href}"${cls}>${ch.icon} ${ch.title}</a>`;
    }).join('');
  }

  const sectionList = document.querySelector('.handbook-section-list');
  if (sectionList && chapterId) {
    const ch = nav.chapters.find(c => c.id === chapterId);
    if (ch) {
      sectionList.innerHTML = ch.sections.map(sec => {
        const href = prefix + `chapters/${ch.id}/${sec.slug}.html`;
        const cls = sec.slug === sectionSlug ? ' class="current-page"' : '';
        return `<a href="${href}"${cls}>${sec.title}</a>`;
      }).join('');
    }
  }

  if (chapterId && sectionSlug) {
    const ch = nav.chapters.find(c => c.id === chapterId);
    if (ch) {
      const idx = ch.sections.findIndex(s => s.slug === sectionSlug);
      const prev = idx > 0 ? ch.sections[idx - 1] : null;
      const next = idx >= 0 && idx < ch.sections.length - 1 ? ch.sections[idx + 1] : null;
      const prevEl = document.querySelector('[data-nav-prev]');
      const nextEl = document.querySelector('[data-nav-next]');
      if (prevEl) {
        if (prev) {
          prevEl.href = prefix + `chapters/${ch.id}/${prev.slug}.html`;
          prevEl.textContent = '← ' + prev.title;
          prevEl.style.visibility = 'visible';
        } else {
          prevEl.href = prefix + ch.index;
          prevEl.textContent = '← Bölüm özeti';
        }
      }
      if (nextEl) {
        if (next) {
          nextEl.href = prefix + `chapters/${ch.id}/${next.slug}.html`;
          nextEl.textContent = next.title + ' →';
        } else {
          const chIdx = nav.chapters.findIndex(c => c.id === chapterId);
          const nextCh = nav.chapters[chIdx + 1];
          if (nextCh) {
            nextEl.href = prefix + nextCh.index;
            nextEl.textContent = nextCh.title + ' →';
          } else {
            nextEl.style.visibility = 'hidden';
          }
        }
      }
    }
  }

  injectHandbookPageTop(prefix, chapterId, sectionSlug, nav);
  enrichTopicListNotebookLinks(prefix, nav, chapterId);
  initNotebookDownloads();
}

function getHandbookStickyTop() {
  let el = document.querySelector('.handbook-sticky-top');
  if (el) return el;
  el = document.createElement('div');
  el.className = 'handbook-sticky-top';
  const nav = document.querySelector('.top-nav');
  if (nav) nav.insertAdjacentElement('afterend', el);
  else document.body.insertBefore(el, document.body.firstChild);
  return el;
}

function buildNotebookBannerHtml(prefix, sec, ch) {
  if (!sec?.notebook) return '';
  const href = prefix + 'notebooks/' + sec.notebook;
  const fname = sec.notebook.split('/').pop();
  return `
    <div class="handbook-notebook-banner handbook-notebook-banner-compact">
      <div class="handbook-notebook-banner-body">
        <span class="handbook-notebook-banner-title">${navEscapeHtml(sec.title)}</span>
        <code class="handbook-notebook-filename">${navEscapeHtml(fname)}</code>
      </div>
      <a href="${href}" download="${navEscapeHtml(fname)}" class="handbook-notebook-dl-btn" title="${navEscapeHtml(fname)} indir">
        📥 İndir
      </a>
    </div>
  `;
}

function buildEnvNoticesHtml() {
  return `
    <details class="handbook-page-tips">
      <summary>⚙️ Web editörü ≠ Jupyter · kod sırası hatırlatması</summary>
      <div class="handbook-page-tips-body">
        <p>Kod editörleri tarayıcıda <strong>Pyodide</strong> ile saf Python çalıştırır — tam Jupyter değildir.
        <code>?</code>, <code>%timeit</code>, <code>!</code> gibi IPython özellikleri web'de çalışmaz.</p>
        <p>Kod blokları <strong>yukarıdan aşağı</strong> birbirine bağımlıdır. Tam deneyim için yukarıdaki notebook'u JupyterLab, VS Code veya Colab'da açıp hücreleri sırayla çalıştırın (<kbd>Shift</kbd>+<kbd>Enter</kbd>).</p>
      </div>
    </details>
  `;
}

function injectHandbookPageTop(prefix, chapterId, sectionSlug, nav) {
  const main = document.querySelector('.handbook-content');

  if (chapterId && sectionSlug) {
    const { ch, sec } = findSectionMeta(nav, chapterId, sectionSlug);
    if (!sec?.notebook || document.querySelector('.handbook-notebook-strip')) return;

    const strip = document.createElement('div');
    strip.className = 'handbook-notebook-strip';
    strip.innerHTML = buildNotebookBannerHtml(prefix, sec, ch);
    getHandbookStickyTop().appendChild(strip);
    document.body.classList.add('has-handbook-nb-strip');

    if (main && !main.querySelector('.handbook-page-top')) {
      const tips = document.createElement('div');
      tips.className = 'handbook-page-top';
      tips.innerHTML = buildEnvNoticesHtml();
      main.insertBefore(tips, main.firstChild);
    }
    return;
  }

  if (chapterId && !sectionSlug && main && !main.querySelector('.handbook-page-top')) {
    const ch = nav.chapters.find(c => c.id === chapterId);
    if (!ch) return;

    const items = ch.sections
      .filter(sec => sec.notebook)
      .map(sec => {
        const fname = sec.notebook.split('/').pop();
        const href = prefix + 'notebooks/' + sec.notebook;
        const pageHref = prefix + `chapters/${ch.id}/${sec.slug}.html`;
        return `<li>
          <a href="${pageHref}">${navEscapeHtml(sec.title)}</a>
          <a href="${href}" download="${navEscapeHtml(fname)}" class="topic-nb-link" title="${navEscapeHtml(fname)}">
            <span class="topic-nb-icon">📥</span><code class="topic-nb-fname">${navEscapeHtml(fname)}</code>
          </a>
        </li>`;
      })
      .join('');

    if (!document.querySelector('.handbook-notebook-strip')) {
      const strip = document.createElement('div');
      strip.className = 'handbook-notebook-strip';
      strip.innerHTML = `
        <div class="handbook-notebook-banner handbook-notebook-banner-chapter">
          <div class="handbook-notebook-banner-icon" aria-hidden="true">📚</div>
          <div class="handbook-notebook-banner-body">
            <div class="handbook-notebook-banner-kicker">Bu bölümün Jupyter notebook'ları</div>
            <div class="handbook-notebook-banner-title">${navEscapeHtml(ch.title)}</div>
            <p class="handbook-notebook-banner-desc">Her konu için ayrı <code>.ipynb</code> — dosya adları aşağıda listelenmiştir.</p>
          </div>
        </div>`;
      getHandbookStickyTop().appendChild(strip);
    }

    const top = document.createElement('div');
    top.className = 'handbook-page-top';
    top.innerHTML = `<ul class="handbook-chapter-nb-list">${items}</ul>`;
    main.insertBefore(top, main.firstChild);
  }
}

function enrichTopicListNotebookLinks(prefix, nav, pageChapterId) {
  document.querySelectorAll('.handbook-topic-list a[href$=".html"]').forEach(link => {
    const href = link.getAttribute('href') || '';
    let chapterId = pageChapterId;
    let slug = '';

    const fullMatch = href.match(/chapters\/([^/]+)\/([^/]+)\.html$/);
    if (fullMatch) {
      chapterId = fullMatch[1];
      slug = fullMatch[2];
    } else {
      slug = href.replace(/^\.\//, '').replace(/\.html$/, '');
    }

    if (!chapterId || !slug) return;

    const { sec } = findSectionMeta(nav, chapterId, slug);
    if (!sec?.notebook) return;

    const li = link.closest('li');
    if (!li) return;

    li.querySelectorAll('a[href$=".ipynb"]').forEach(a => a.remove());

    const fname = sec.notebook.split('/').pop();
    const nbHref = prefix + 'notebooks/' + sec.notebook;
    const dl = document.createElement('a');
    dl.href = nbHref;
    dl.download = fname;
    dl.className = 'topic-nb-link';
    dl.title = `${sec.title} — ${fname}`;
    dl.innerHTML = `<span class="topic-nb-icon">📥</span><code class="topic-nb-fname">${fname}</code>`;

    if (li.lastChild === link) {
      li.appendChild(document.createTextNode(' '));
      li.appendChild(dl);
    } else {
      li.appendChild(document.createTextNode(' '));
      li.appendChild(dl);
    }
  });
}

function notebookFilenameFromHref(href) {
  const clean = (href || '').split('?')[0].split('#')[0];
  const name = clean.split('/').pop();
  return name && name.endsWith('.ipynb') ? name : 'notebook.ipynb';
}

async function triggerNotebookDownload(e) {
  if (e.metaKey || e.ctrlKey || e.shiftKey || e.altKey || e.button !== 0) return;

  const link = e.currentTarget;
  const href = link.getAttribute('href');
  if (!href || !href.includes('.ipynb')) return;

  e.preventDefault();

  const filename = link.getAttribute('download') || notebookFilenameFromHref(href);
  if (link.dataset.nbBusy === 'true') return;

  link.dataset.nbBusy = 'true';
  const prevPointer = link.style.pointerEvents;
  link.style.pointerEvents = 'none';

  try {
    const resp = await fetch(href, { credentials: 'same-origin' });
    if (!resp.ok) throw new Error(`HTTP ${resp.status}`);
    const buffer = await resp.arrayBuffer();
    const blob = new Blob([buffer], { type: 'application/octet-stream' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = filename;
    a.rel = 'noopener';
    a.style.display = 'none';
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
  } catch (err) {
    console.error('Notebook indirme hatası:', err);
  } finally {
    delete link.dataset.nbBusy;
    link.style.pointerEvents = prevPointer;
  }
}

function initNotebookDownloads() {
  document.querySelectorAll('.pds-handbook-site a[href$=".ipynb"]').forEach(link => {
    if (link.dataset.nbDownloadBound === 'true') return;
    link.dataset.nbDownloadBound = 'true';
    if (!link.getAttribute('download')) {
      link.setAttribute('download', notebookFilenameFromHref(link.getAttribute('href')));
    }
    link.addEventListener('click', triggerNotebookDownload);
  });
}

document.addEventListener('DOMContentLoaded', initHandbookNav);
