#!/usr/bin/env python3
"""Build Turkish HTML bodies for Pandas chapters 3.1 and 3.2 from source notebooks."""
from __future__ import annotations

import html
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TOOLS = Path(__file__).resolve().parent
sys.path.insert(0, str(TOOLS))

from write_pandas_chapter import write_chapter

# --- markdown helpers ---

def slugify(text: str) -> str:
    text = re.sub(r"`([^`]+)`", r"\1", text)
    text = text.strip().lower()
    tr = str.maketrans(
        "çğıöşüâîû",
        "cgiosuaiu",
    )
    text = text.translate(tr)
    text = re.sub(r"[^a-z0-9\s-]", "", text)
    text = re.sub(r"\s+", "-", text).strip("-")
    return text or "bolum"


def esc_code(s: str) -> str:
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def md_inline(s: str) -> str:
    s = html.escape(s, quote=False)
    s = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"\*([^*]+)\*", r"<em>\1</em>", s)
    s = re.sub(r"``([^`]+)``", r"<code>\1</code>", s)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    s = re.sub(
        r"\[([^\]]+)\]\(([^)]+)\)",
        lambda m: f'<a href="{html.escape(_fix_link(m.group(2)), quote=True)}">{m.group(1)}</a>',
        s,
    )
    return s


def _fix_link(href: str) -> str:
    mapping = {
        "02.00-Introduction-to-NumPy.ipynb": "../02-numpy/00-introduction.html",
        "01-introducing-pandas-objects.html": "01-introducing-pandas-objects.html",
        "02.09-Structured-Data-NumPy.ipynb": "../02-numpy/09-structured-arrays.html",
        "03.02-Data-Indexing-and-Selection.ipynb": "02-data-indexing-and-selection.html",
        "03.03-Operations-in-Pandas.ipynb": "03-operations-in-pandas.html",
        "03.04-Missing-Values.ipynb": "04-missing-values.html",
    }
    if href in mapping:
        return mapping[href]
    if href.startswith("http"):
        return href
    return href


def md_block(text: str) -> str:
    lines = text.strip().split("\n")
    out: list[str] = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.startswith("```"):
            lang = line[3:].strip() or "python"
            i += 1
            code_lines = []
            while i < len(lines) and not lines[i].startswith("```"):
                code_lines.append(lines[i])
                i += 1
            i += 1
            code = esc_code("\n".join(code_lines))
            fn = "ornek.py" if lang == "python" else "ornek.txt"
            out.append(
                f'    <motionless class="code-block" data-lang="{lang}" data-filename="{fn}">'
            )
            out.append(f"      <pre><code>{code}</code></pre>")
            out.append("    </div>")
            continue
        if line.startswith("#### "):
            t = line[5:].strip()
            out.append(f'    <h4 id="{slugify(t)}">{md_inline(t)}</h4>')
        elif line.startswith("### "):
            t = line[4:].strip()
            out.append(f'    <h3 id="{slugify(t)}">{md_inline(t)}</h3>')
        elif line.startswith("## "):
            t = line[3:].strip()
            out.append(f'    <h2 id="{slugify(t)}">{md_inline(t)}</h2>')
        elif line.startswith("# "):
            pass  # h1 handled separately
        elif line.strip() == "":
            pass
        else:
            para = []
            while i < len(lines) and lines[i].strip() and not lines[i].startswith("#"):
                para.append(lines[i])
                i += 1
            out.append(f"    <p>{md_inline(' '.join(para))}</p>")
            continue
        i += 1
    # fix typo motionless -> div (editor safety)
    return "\n".join(out).replace("<motionless", "<motionless").replace(
        '<motionless class="code-block"', '<motionless'
    ).replace("<motionless", "<div").replace("motionless>", "motionless>")


def code_block(code: str, filename: str, readonly: bool = False, lang: str = "python") -> str:
    attrs = f'data-lang="{lang}" data-filename="{html.escape(filename)}"'
    if readonly:
        attrs += ' data-readonly="true"'
    esc = esc_code(code.rstrip("\n"))
    return f"""    <motionless class="code-block" {attrs}>
      <pre><code>{esc}</code></pre>
    </div>""".replace("<motionless", "<div").replace("motionless>", "div>")


def output_block(text: str, in_num: int | None = None) -> str:
    prefix = f"In [{in_num}]:\n" if in_num else ""
    body = prefix + text.rstrip() + "\n"
    return code_block(body, "ipython_cikti.txt", readonly=True, lang="text")


def tip(title: str, body: str) -> str:
    return f"""    <div class="alert alert-tip handbook-addon">
      <motionless class="alert-title">💡 Ders notu — {html.escape(title)}</motionless>
      <p>{md_inline(body)}</p>
    </motionless>""".replace("<motionless", "<motionless").replace("<motionless", "<div").replace(
        "motionless>", "div>"
    )


def try_it(title: str, desc: str, code: str, filename: str) -> str:
    return f"""    <div class="try-it-box">
      <div class="try-it-title">🧪 {html.escape(title)}</div>
      <p>{md_inline(desc)}</p>
      {code_block(code, filename)}
    </div>"""


def _strip_ansi(text: str) -> str:
    text = re.sub(r"\x1b\[[0-9;]*m", "", text)
    text = re.sub(r"\[[0-9;]*m", "", text)  # bazen ESC kaybolmuş olur
    return text


def get_output(cell: dict) -> str | None:
    parts = []
    for o in cell.get("outputs", []):
        if o.get("output_type") == "execute_result":
            data = o.get("data", {})
            if "text/plain" in data:
                parts.append("".join(data["text/plain"]))
        elif o.get("output_type") == "stream":
            parts.append("".join(o.get("text", [])))
        elif o.get("output_type") == "error":
            parts.append(f"{o.get('ename', 'Error')}: {o.get('evalue', '')}")
    if not parts:
        return None
    return _strip_ansi("".join(parts))


# Turkish markdown per cell index
TR_301: dict[int, str] = {
    0: "",  # h1 separate
    1: """En temel düzeyde Pandas nesneleri, satır ve sütunların basit tamsayı indeksleri yerine etiketlerle tanımlandığı NumPy yapılandırılmış dizilerinin geliştirilmiş sürümleri olarak düşünülebilir.
Bu bölüm boyunca göreceğimiz gibi Pandas, temel veri yapılarının üzerine birçok yararlı araç, yöntem ve işlev sunar; ancak bundan sonraki hemen her şey bu yapıların ne olduğunu anlamayı gerektirir.
Bu yüzden daha ileri gitmeden önce üç temel Pandas veri yapısına bakalım: `Series`, `DataFrame` ve `Index`.

Kod oturumlarına standart NumPy ve Pandas içe aktarmalarıyla başlayacağız:""",
    3: """## Pandas Series Nesnesi

Pandas `Series`, indekslenmiş veriden oluşan tek boyutlu bir dizidir.
Liste veya dizi ile şöyle oluşturulabilir:""",
    5: """`Series`, bir değer dizisini açık bir indeks dizisiyle birleştirir; `values` ve `index` öznitelikleriyle erişilir.
`values` tanıdık bir NumPy dizisidir:""",
    7: """`index`, `pd.Index` tipinde dizi benzeri bir nesnedir; birazdan ayrıntılandıracağız:""",
    9: """NumPy dizisinde olduğu gibi, veriye ilişkili indeks üzerinden Python köşeli parantez gösterimiyle erişilebilir:""",
    12: """Göreceğimiz üzere Pandas `Series`, taklit ettiği tek boyutlu NumPy dizisinden çok daha genel ve esnektir.""",
    13: "### Series, Genelleştirilmiş NumPy Dizisi",
    14: """Şimdiye kadar gördüklerimizden `Series` nesnesi tek boyutlu bir NumPy dizisiyle neredeyse değiştirilebilir görünebilir.
Temel fark şudur: NumPy dizisinde değerlere erişmek için *örtük* tamsayı indeks kullanılır; Pandas `Series`'te ise değerlerle birlikte *açık* bir indeks tanımlıdır.

Bu açık indeks, `Series`'e ek yetenekler verir. Örneğin indeks tamsayı olmak zorunda değildir; istenen herhangi bir türde olabilir.
İstersek string indeks kullanabiliriz:""",
    16: "Öğe erişimi beklendiği gibi çalışır:",
    18: "Ardışık olmayan veya sıralı olmayan indeksler de kullanılabilir:",
    21: """### Series, Özelleştirilmiş Sözlük

Bu bakışla Pandas `Series`, Python sözlüğünün bir özelleşmesi gibi düşünülebilir.
Sözlük key → değer eşlemesi yapar; `Series` ise tipli anahtarları tipli değerlere eşler.
Bu tip bilgisi önemlidir: NumPy dizisinin arkasındaki tip odaklı derlenmiş kod, belirli işlemlerde Python listesinden daha verimli kılar; `Series`'in tip bilgisi de benzer şekilde Python sözlüklerinden daha verimli olmasını sağlar.

`Series`-sözlük benzetmesi, doğrudan Python sözlüğünden `Series` oluşturarak netleşir — burada 2020 nüfus sayımına göre ABD'nin en kalabalık beş eyaleti:""",
    23: "Buradan tipik sözlük tarzı öğe erişimi yapılabilir:",
    25: "Sözlükten farklı olarak `Series` dilimleme gibi dizi tarzı işlemleri de destekler:",
    27: "Pandas indeksleme ve dilimlemenin bazı inceliklerini [Veri İndeksleme ve Seçimi](03.02-Data-Indexing-and-Selection.ipynb) bölümünde ele alacağız.",
    28: """### Series Nesneleri Oluşturma

Sıfırdan `Series` oluşturmanın birkaç yolunu gördük; hepsi şu kalıba benzer:

```python
pd.Series(data, index=index)
```

`index` isteğe bağlıdır; `data` birçok türden biri olabilir.

Örneğin `data` liste veya NumPy dizisi olabilir; bu durumda `index` varsayılan olarak tamsayı dizisidir:""",
    30: "Ya da `data` bir skaler olabilir; belirtilen indekste tekrarlanır:",
    32: "Ya da sözlük olabilir; `index` varsayılan olarak sözlük anahtarlarıdır:",
    34: "Her durumda indeks, sırayı veya kullanılacak anahtar alt kümesini açıkça belirlemek için ayarlanabilir:",
    36: """## Pandas DataFrame Nesnesi

Pandas'taki bir sonraki temel yapı `DataFrame`'dir.
Önceki bölümdeki `Series` gibi `DataFrame` hem NumPy dizisinin genellemesi hem de Python sözlüğünün özelleşmesi olarak düşünülebilir.
Her iki bakış açısını da inceleyeceğiz.""",
    37: """### DataFrame, Genelleştirilmiş NumPy Dizisi

`Series` açık indeksli tek boyutlu dizi analoguysa, `DataFrame` açık satır ve sütun indeksli iki boyutlu dizi analogudur.
İki boyutlu diziyi hizalı tek boyutlu sütunların sıralı dizisi gibi düşünürseniz, `DataFrame`'i hizalı `Series` nesnelerinin dizisi olarak düşünebilirsiniz.
“Hizalı” derken aynı indeksi paylaştıklarını kastediyoruz.

Bunu göstermek için önceki bölümdeki beş eyaletin alanını (km²) listeleyen yeni bir `Series` oluşturalım:""",
    39: "Bunu ve önceki `population` `Series`'ini kullanarak bu bilgiyi içeren tek bir iki boyutlu nesne oluşturabiliriz:",
    41: "`Series` gibi `DataFrame`'in de indeks etiketlerine erişen bir `index` özniteliği vardır:",
    43: "Ayrıca sütun etiketlerini tutan `Index` tipinde bir `columns` özniteliği vardır:",
    45: "Böylece `DataFrame`, hem satır hem sütunların veriye erişim için genelleştirilmiş indekse sahip olduğu iki boyutlu NumPy dizisinin genellemesi olarak görülebilir.",
    46: """### DataFrame, Özelleştirilmiş Sözlük

Benzer şekilde `DataFrame` bir sözlük özelleşmesi olarak da düşünülebilir.
Sözlük anahtar → değer eşler; `DataFrame` sütun adı → sütun verisinin `Series`'i eşler.
Örneğin `'area'` istendiğinde daha önce gördüğümüz alan `Series`'i döner:""",
    48: """Burada kafa karıştırıcı bir nokta olabilir: iki boyutlu NumPy dizisinde `data[0]` ilk *satırı* döndürür; `DataFrame`'de `data['col0']` ilk *sütunu* döndürür.
Bu yüzden `DataFrame`'i genelleştirilmiş dizi yerine genelleştirilmiş sözlük olarak düşünmek genelde daha iyidir; her iki bakış da yararlı olabilir.
`DataFrame` için daha esnek indekslemeyi [Veri İndeksleme ve Seçimi](03.02-Data-Indexing-and-Selection.ipynb) bölümünde inceleyeceğiz.""",
    49: """### DataFrame Nesneleri Oluşturma

Pandas `DataFrame` birçok yolla oluşturulabilir.
Burada birkaç örneği ele alıyoruz.""",
    50: """#### Tek bir Series nesnesinden

`DataFrame`, `Series` nesnelerinin koleksiyonudur; tek sütunlu `DataFrame` tek bir `Series`'ten oluşturulabilir:""",
    52: """#### Sözlük listesinden

Herhangi bir sözlük listesi `DataFrame` yapılabilir.
Basit bir list comprehension ile veri üretelim:""",
    54: """Sözlüklerde bazı anahtarlar eksik olsa bile Pandas eksikleri `NaN` (Not a Number) ile doldurur; bkz. [Eksik Veri](03.04-Missing-Values.ipynb):""",
    56: "Daha önce gördüğümüz gibi `DataFrame`, `Series` sözlüğünden de oluşturulabilir:",
    58: """#### İki boyutlu NumPy dizisinden

İki boyutlu veri dizisi verildiğinde istenen sütun ve indeks adlarıyla `DataFrame` oluşturulabilir.
Belirtilmezse her biri için tamsayı indeks kullanılır:""",
    60: """#### NumPy yapılandırılmış dizisinden

Yapılandırılmış dizileri [Yapılandırılmış Veri: NumPy Yapılandırılmış Dizileri](02.09-Structured-Data-NumPy.ipynb) bölümünde ele aldık.
Pandas `DataFrame` yapılandırılmış diziye çok benzer çalışır ve doğrudan ondan oluşturulabilir:""",
    63: """## Pandas Index Nesnesi

Gördüğünüz gibi `Series` ve `DataFrame` veriye referans ve değişiklik için açık bir *indeks* içerir.
`Index` kendi başına ilginç bir yapıdır; *değiştirilemez dizi* veya *sıralı küme* (teknik olarak çok küme — `Index` tekrarlı değer içerebilir) olarak düşünülebilir.
Bu görünümler `Index` üzerindeki işlemlere ilginç sonuçlar verir.
Basit örnek: tamsayı listesinden `Index` oluşturalım:""",
    65: """### Index, Değiştirilemez Dizi

`Index` birçok yönden dizi gibi davranır.
Standart Python indeks gösterimiyle değer veya dilim alınabilir:""",
    68: "`Index` nesneleri NumPy dizilerinden tanıdık birçok özniteliğe de sahiptir:",
    70: "`Index` ile NumPy dizisi arasındaki farklardan biri indekslerin değiştirilemez olmasıdır — normal yollarla değiştirilemezler:",
    72: "Bu değişmezlik, birden fazla `DataFrame` ve dizi arasında indeks paylaşmayı daha güvenli kılar; istemeden indeks değişikliğinin yan etkileri olmaz.",
    73: """### Index, Sıralı Küme

Pandas nesneleri veri kümeleri arasında birleştirme gibi küme aritmetiğine dayanan işlemleri kolaylaştıracak şekilde tasarlanmıştır.
`Index`, Python'un yerleşik `set` yapısının birçok kuralını izler; birleşim, kesişim, fark ve diğer kombinasyonlar tanıdık biçimde hesaplanabilir:""",
}

TR_302: dict[int, str] = {
    0: "",
    1: """[Bölüm 2](02.00-Introduction-to-NumPy.ipynb)'de NumPy dizilerinde değerlere erişme, atama ve değiştirme araçlarını ayrıntılı inceledik.
Bunlar arasında indeksleme (`arr[2, 1]`), dilimleme (`arr[:, 1:5]`), maskeleme (`arr[arr > 0]`), fancy indexing (`arr[0, [1, 5]]`) ve bunların birleşimleri (`arr[:, [1, 5]]`) vardı.
Burada Pandas `Series` ve `DataFrame` nesnelerinde benzer erişim ve değiştirme kalıplarına bakacağız.
NumPy kalıplarını biliyorsanız Pandas'taki karşılıkları çok tanıdık gelecektir; yine de bilmeniz gereken birkaç incelik vardır.

Önce tek boyutlu `Series` ile başlayıp ardından iki boyutlu `DataFrame`'e geçeceğiz.""",
    2: """## Series'te Veri Seçimi

Önceki bölümde gördüğünüz gibi `Series` hem tek boyutlu NumPy dizisine hem de standart Python sözlüğüne benzer.
Bu iki örtüşen benzetmeyi aklınızda tutarsanız bu yapılarda indeksleme ve seçim kalıplarını anlamanız kolaylaşır.""",
    3: """### Series, Sözlük Olarak

Sözlük gibi `Series`, anahtar koleksiyonundan değer koleksiyonuna eşleme sağlar:""",
    6: "Anahtar/indeks ve değerleri incelemek için sözlük benzeri Python ifadeleri ve yöntemleri de kullanılabilir:",
    10: """`Series` nesneleri sözlük benzeri sözdizimiyle de değiştirilebilir.
Sözlüğe yeni anahtar atayarak genişlettiğiniz gibi, yeni indeks değerine atayarak `Series`'i genişletebilirsiniz:""",
    12: "Nesnelerin bu kolay değiştirilebilirliği kullanışlı bir özelliktir: Pandas arka planda bellek düzeni ve veri kopyalama kararlarını verir; kullanıcı genelde bu konularla uğraşmak zorunda kalmaz.",
    13: "### Series, Tek Boyutlu Dizi Olarak",
    14: """`Series`, bu sözlük benzeri arayüzün üzerine NumPy dizilerindeki gibi dilimleme, maskeleme ve fancy indexing ile dizi tarzı seçim sunar.
Örnekler:""",
    19: """Bunların içinde en çok kafa karıştıran dilimleme olabilir.
Açık indeksle dilimlerken (ör. `data['a':'c']`) son indeks dilime *dahildir*; örtük indeksle dilimlerken (ör. `data[0:2]`) son indeks dilime *dahil değildir*.""",
    20: """### İndeksleyiciler: loc ve iloc

`Series`'in açık tamsayı indeksi varsa `data[1]` gibi indeksleme açık indeksi, `data[1:3]` gibi dilimleme ise örtük Python tarzı indeksi kullanır:""",
    24: """Tamsayı indekslerde bu karışıklık riski nedeniyle Pandas belirli indeksleme şemalarını açıkça sunan özel *indeksleyici* öznitelikleri sağlar.
Bunlar fonksiyon değil; `Series` içindeki veriye belirli bir dilim arayüzü sunan özniteliklerdir.

`loc` özniteliği her zaman açık indeksi referans alan indeksleme ve dilimlemeye izin verir:""",
    27: "`iloc` özniteliği her zaman örtük Python tarzı indeksi referans alır:",
    30: """Python'da “açık, örtükten iyidir” ilkesi geçerlidir.
`loc` ve `iloc`'un açık doğası kodu okunaklı tutar; özellikle tamsayı indekslerde tutarlı kullanım, karışık indeksleme/dilimleme kurallarından kaynaklanan ince hataları önler.""",
    31: """## DataFrame'de Veri Seçimi

`DataFrame` hem iki boyutlu veya yapılandırılmış diziye hem de aynı indeksi paylaşan `Series` sözlüğüne benzer.
Bu benzetmeler veri seçimini keşfederken yardımcı olur.""",
    32: """### DataFrame, Sözlük Olarak

İlk benzetme: `DataFrame`, ilişkili `Series` nesnelerinin sözlüğü.
Eyalet alan ve nüfus örneğimize dönelim:""",
    34: "`DataFrame` sütunlarını oluşturan `Series`'lere sütun adıyla sözlük tarzı erişilir:",
    36: "Eşdeğer olarak, string sütun adları için öznitelik tarzı erişim de mümkündür:",
    38: """Bu kısayol kullanışlı olsa da her durumda çalışmaz!
Sütun adları string değilse veya `DataFrame` yöntemleriyle çakışıyorsa öznitelik erişimi mümkün olmayabilir.
Örneğin `DataFrame`'in bir `pop` yöntemi vardır; `data.pop` sütun yerine bu yönteme işaret eder:""",
    40: """Özellikle sütun atamayı öznitelikle yapmaktan kaçının (`data.pop = z` yerine `data['pop'] = z` kullanın).

Daha önceki `Series` gibi bu sözlük sözdizimi nesneyi değiştirmek için kullanılır; burada yeni sütun eklenir:""",
    42: "Bu, `Series` nesneleri arasında eleman-eleman aritmetiğin sade sözdizimine bir ön izlemedir; ayrıntı için [Pandas'ta İşlemler](03.03-Operations-in-Pandas.ipynb) bölümüne bakın.",
    43: """### DataFrame, İki Boyutlu Dizi Olarak

Daha önce belirtildiği gibi `DataFrame` geliştirilmiş iki boyutlu dizi olarak da görülebilir.
Ham veri dizisine `values` özniteliğiyle bakılabilir:""",
    45: "Bu bakışla `DataFrame` üzerinde birçok tanıdık dizi benzeri işlem yapılabilir; örneğin tam `DataFrame` transpoze edilerek satır ve sütunlar yer değiştirilebilir:",
    47: """`DataFrame` indekslemesinde ise sütunların sözlük tarzı indekslenmesi onu doğrudan NumPy dizisi gibi ele almayı engeller.
Özellikle diziye tek indeks verildiğinde satıra erişilir:""",
    49: "`DataFrame`'e tek “indeks” verildiğinde ise sütuna erişilir:",
    51: """Dizi tarzı indeksleme için başka bir kural gerekir.
Pandas yine `loc` ve `iloc` indeksleyicilerini kullanır.
`iloc` ile alttaki dizi NumPy dizisi gibi indekslenir (örtük Python indeksi); sonuçta `DataFrame` indeks ve sütun etiketleri korunur:""",
    53: "`loc` ile veri açık indeks ve sütun adlarıyla dizi benzeri indekslenir:",
    55: "Bu indeksleyiciler içinde tanıdık NumPy tarzı erişim kalıpları kullanılabilir; `loc` içinde maskeleme ve fancy indexing birleştirilebilir:",
    57: "Bu indeksleme kuralları değer atamak veya değiştirmek için de kullanılır; NumPy'de alışık olduğunuz standart yolla:",
    59: "Pandas veri manipülasyonunda akıcılık için basit bir `DataFrame` ile bu indeksleme yaklaşımlarının izin verdiği indeksleme, dilimleme, maskeleme ve fancy indexing türlerini denemenizi öneririm.",
    60: """### Ek İndeksleme Kuralları

Önceki tartışmayla çelişiyor gibi görünen ama pratikte yararlı birkaç ek kural vardır.
Önce: *indeksleme* sütunlara, *dilimleme* satırlara referans verir:""",
    62: "Bu dilimler indeks yerine satır numarasıyla da yapılabilir:",
    64: "Benzer şekilde doğrudan maskeleme sütun yerine satır bazında yorumlanır:",
    66: "Bu iki kural NumPy dizisindekine sözdizimsel olarak benzer; Pandas kurallarına tam uymasa da pratik faydaları nedeniyle dahil edilmiştir.",
}


def build_chapter(nb_path: Path, slug: str, h1: str, en_title: str, en_url: str,
                  tr_map: dict[int, str], extras: list[str], next_link: str) -> tuple[int, int]:
    nb = json.loads(nb_path.read_text(encoding="utf-8"))
    parts: list[str] = []
    parts.append(f"<h1>{html.escape(h1)}</h1>")
    parts.append(
        f'    <p><em>Orijinal: <a href="{html.escape(en_url)}" target="_blank" rel="noopener">'
        f"{html.escape(en_title)}</a></em></p>"
    )
    code_count = 0
    in_counter = 0
    for i, cell in enumerate(nb["cells"]):
        if cell["cell_type"] == "markdown":
            tr = tr_map.get(i)
            if tr is None:
                src = "".join(cell["source"])
                tr = src  # fallback EN
            if i == 0:
                continue
            parts.append(md_block(tr))
        elif cell["cell_type"] == "code":
            code = "".join(cell["source"]).rstrip("\n")
            if not code.strip():
                continue
            code_count += 1
            in_counter += 1
            fn = f"hucere_{i}.py"
            parts.append(code_block(code, fn))
            out = get_output(cell)
            if out:
                parts.append(output_block(out, in_counter))
    parts.extend(extras)
    parts.append(f"""    <motionless class="alert alert-info">
      <div class="alert-title">🔗 Sonraki konu</motionless>
      <p><a href="{html.escape(next_link)}">{html.escape(next_link)}</a></p>
    </motionless>""".replace("<motionless", "<motionless").replace("<motionless", "<div").replace("motionless>", "motionless>"))
    body = "\n\n".join(parts).replace("<motionless", "<div").replace("motionless>", "div>")
    write_chapter(slug, body)
    return len(nb["cells"]), code_count


EXTRAS_301 = [
    tip(
        "Series vs NumPy",
        "`Series.values` her zaman NumPy dizisidir; indeks bilgisi `Series.index`'te kalır. Hesap için çoğu zaman `.values` veya doğrudan vektörize Pandas işlemleri kullanılır.",
    ),
    try_it(
        "Şimdi deneyin",
        "String indeksli bir `Series` oluşturup `loc` ile dilimleyin:",
        "import pandas as pd\ns = pd.Series([10, 20, 30], index=list('abc'))\nprint(s.loc['a':'b'])",
        "series_loc_deneme.py",
    ),
    tip(
        "DataFrame sütun vs satır",
        "NumPy'de `arr[0]` ilk satırdır; `DataFrame`'de `df['sütun']` bir sütun `Series`'idir. Karışıklığı önlemek için sütun seçiminde her zaman köşeli parantez kullanın.",
    ),
    try_it(
        "Şimdi deneyin",
        "İki sütunlu küçük bir `DataFrame` oluşturup `states['area']` ile sütun seçin:",
        "import pandas as pd\nstates = pd.DataFrame({\n    'nufus': pd.Series({'A': 100, 'B': 200}),\n    'alan': pd.Series({'A': 50, 'B': 80}),\n})\nprint(states['alan'])",
        "dataframe_sutun.py",
    ),
    tip(
        "Index değişmezliği",
        "`Index` öğeleri atama ile değiştirilemez; bu paylaşılan indekslerde yan etkiyi azaltır. Değişiklik gerekiyorsa yeni `Index` oluşturun.",
    ),
    tip(
        "Index küme işlemleri",
        "`indA & indB` kesişim, `|` birleşim, `^` simetrik fark verir. Aynı işlemler `.intersection()`, `.union()`, `.symmetric_difference()` ile de yapılır.",
    ),
]

EXTRAS_302 = [
    tip(
        "Açık vs örtük dilim",
        "`data['a':'c']` son etiketi dahil eder; `data[0:2]` Python dilimi gibi sonu hariç tutar. Karışıklıkta `loc` / `iloc` kullanın.",
    ),
    try_it(
        "Şimdi deneyin",
        "Tamsayı indeksli `Series` ile `loc` ve `iloc` farkını deneyin:",
        "import pandas as pd\ndata = pd.Series(['x', 'y', 'z'], index=[10, 20, 30])\nprint('loc[20]:', data.loc[20])\nprint('iloc[1]:', data.iloc[1])",
        "loc_iloc_deneme.py",
    ),
    tip(
        "data.pop tuzağı",
        "`DataFrame.pop` bir yöntemdir; `pop` sütununa `data['pop']` ile erişin. Sütun atamada asla `data.pop = ...` kullanmayın.",
    ),
    try_it(
        "Şimdi deneyin",
        "Eyalet verisiyle `density` sütunu ekleyin ve `loc` ile filtreleyin:",
        "import pandas as pd\narea = pd.Series({'CA': 400, 'TX': 700})\npop = pd.Series({'CA': 40, 'TX': 30})\ndf = pd.DataFrame({'area': area, 'pop': pop})\ndf['density'] = df['pop'] / df['area']\nprint(df.loc[df['density'] > 0.05])",
        "dataframe_loc_deneme.py",
    ),
    tip(
        "Satır dilimleme kuralı",
        "`df['Florida':'New York']` satır etiketleri arasında dilimler (son dahil). `df[1:3]` satır numarasına göre dilimler (son hariç).",
    ),
]


def main():
    nb01 = TOOLS / "source/notebooks/03.01-Introducing-Pandas-Objects.ipynb"
    nb02 = TOOLS / "source/notebooks/03.02-Data-Indexing-and-Selection.ipynb"
    # insert extras before footer in build - patch build_chapter to insert extras before next link
    # Rebuild with manual insertion
    for slug, nb, h1, en_t, tr, extras, nxt in [
        ("01-introducing-pandas-objects", nb01, "Pandas Nesnelerine Giriş",
         "Introducing Pandas Objects", TR_301, EXTRAS_301, "02-data-indexing-and-selection.html →"),
        ("02-data-indexing-and-selection", nb02, "Veri İndeksleme ve Seçimi",
         "Data Indexing and Selection", TR_302, EXTRAS_302, "03-operations-in-pandas.html →"),
    ]:
        from pandas_sections import PANDAS_SECTIONS
        sec = next(s for s in PANDAS_SECTIONS if s["slug"] == slug)
        nb_path = nb
        nb_data = json.loads(nb_path.read_text(encoding="utf-8"))
        parts: list[str] = []
        parts.append(f"<h1>{html.escape(h1)}</h1>")
        parts.append(
            f'    <p><em>Orijinal: <a href="{sec["en_url"]}" target="_blank" rel="noopener">'
            f"{html.escape(en_t)}</a></em></p>"
        )
        if slug == "01-introducing-pandas-objects":
            parts.append(
                '    <p><a href="00-introduction.html">Bölüm 3 girişinde</a> Pandas\'ın genel rolünü ele aldık; '
                'burada <code>Series</code>, <code>DataFrame</code> ve <code>Index</code> yapılarına odaklanıyoruz.</p>'
            )
        elif slug == "02-data-indexing-and-selection":
            parts.append(
                '    <p><a href="01-introducing-pandas-objects.html">Önceki bölümde</a> '
                '<code>Series</code>, <code>DataFrame</code> ve <code>Index</code> nesnelerini tanıdık.</p>'
            )
        code_count = 0
        in_counter = 0
        tr_map = tr
        for i, cell in enumerate(nb_data["cells"]):
            if cell["cell_type"] == "markdown":
                if i == 0:
                    continue
                tr_text = tr_map.get(i, "".join(cell["source"]))
                parts.append(md_block(tr_text))
            elif cell["cell_type"] == "code":
                code = "".join(cell["source"]).rstrip("\n")
                if not code.strip():
                    continue
                code_count += 1
                in_counter += 1
                parts.append(code_block(code, f"hucere_{i}.py"))
                out = get_output(cell)
                if out:
                    parts.append(output_block(out, in_counter))
        parts.extend(extras)
        if slug == "01-introducing-pandas-objects":
            parts.append(
                '    <motionless class="alert alert-info"><div class="alert-title">🔗 Sonraki konu</div>'
                '<p><a href="02-data-indexing-and-selection.html">3.2 Veri İndeksleme ve Seçimi →</a></p></motionless>'
            )
        else:
            parts.append(
                '    <motionless class="alert alert-info"><motionless class="alert-title">🔗 Sonraki konu</motionless>'
                '<p><a href="03-operations-in-pandas.html">3.3 Pandas\'ta İşlemler →</a></p></motionless>'
            )
        body = "\n\n".join(parts).replace("<motionless", "<div").replace("motionless>", "div>")
        write_chapter(slug, body)
        print(f"{slug}: cells={len(nb_data['cells'])} code_blocks={code_count}")
    subprocess.run([sys.executable, str(TOOLS / "export_notebooks.py")], check=True, cwd=ROOT)


if __name__ == "__main__":
    main()
