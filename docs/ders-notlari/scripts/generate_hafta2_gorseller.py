#!/usr/bin/env python3
"""Hafta 2 ders notları — infografik görseller (yeniden tasarım)."""
from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch, FancyBboxPatch, Polygon

OUT = Path(__file__).resolve().parent.parent / "images"
OUT.mkdir(parents=True, exist_ok=True)

# Ders sitesi paleti
BG = "#ffffff"
INK = "#0f172a"
MUTED = "#64748b"
SUB = "#475569"

PALETTE = {
    "data": {"main": "#64748b", "soft": "#f1f5f9", "edge": "#94a3b8"},
    "info": {"main": "#0284c7", "soft": "#e0f2fe", "edge": "#38bdf8"},
    "know": {"main": "#2563eb", "soft": "#dbeafe", "edge": "#60a5fa"},
    "wisdom": {"main": "#7c3aed", "soft": "#ede9fe", "edge": "#a78bfa"},
}
def _setup(figsize=(10, 6)):
    fig, ax = plt.subplots(figsize=figsize)
    fig.patch.set_facecolor(BG)
    ax.set_facecolor(BG)
    ax.axis("off")
    return fig, ax


def _save(fig, name: str) -> None:
    path = OUT / name
    fig.savefig(path, dpi=160, bbox_inches="tight", facecolor=BG, edgecolor="none")
    plt.close(fig)
    print("wrote", path)


def _shadow_box(ax, xy, w, h, color, radius=0.12, alpha=0.35, offset=(0.06, -0.06)):
    sx, sy = xy[0] + offset[0], xy[1] + offset[1]
    shadow = FancyBboxPatch(
        (sx, sy), w, h,
        boxstyle=f"round,pad=0.02,rounding_size={radius}",
        facecolor="#cbd5e1", edgecolor="none", alpha=alpha, zorder=1,
    )
    ax.add_patch(shadow)
    box = FancyBboxPatch(
        xy, w, h,
        boxstyle=f"round,pad=0.02,rounding_size={radius}",
        facecolor="white", edgecolor=color, linewidth=2.2, zorder=2,
    )
    ax.add_patch(box)


def _label_block(ax, x, y, w, h, title, subtitle, color, example=None, z=3):
    _shadow_box(ax, (x, y), w, h, color)
    ax.text(x + w / 2, y + h * 0.68, title, ha="center", va="center",
            fontsize=11.5, fontweight="bold", color=color, zorder=z)
    ax.text(x + w / 2, y + h * 0.42, subtitle, ha="center", va="center",
            fontsize=9, color=SUB, zorder=z)
    if example:
        ax.text(x + w / 2, y + h * 0.18, example, ha="center", va="center",
                fontsize=8.2, color=MUTED, style="italic", zorder=z)


def dikw_piramidi() -> None:
    """Gerçek piramit formu + sağda somut tıbbi örnek."""
    fig, ax = _setup((10.5, 7.2))
    ax.set_xlim(0, 10.5)
    ax.set_ylim(0, 7.2)

    ax.text(5.2, 6.75, "DIKW Piramidi", ha="center", fontsize=18, fontweight="bold", color=INK)
    ax.text(5.2, 6.35, "Veri → Enformasyon → Bilgi → Bilgelik", ha="center", fontsize=11, color=MUTED)

    layers = [
        ("BİLGELİK", "Wisdom", "Doğru zamanda doğru karar", PALETTE["wisdom"], 2.2, 1.05, 4.4),
        ("BİLGİ", "Knowledge", "Deneyim + yorum + bağlam", PALETTE["know"], 3.0, 1.05, 3.15),
        ("ENFORMASYON", "Information", "Anlam kazandırılmış veri", PALETTE["info"], 3.8, 1.05, 1.9),
        ("VERİ", "Data", "Ham ölçüm ve gözlemler", PALETTE["data"], 4.6, 1.05, 0.65),
    ]
    cx = 3.35
    for name_tr, name_en, desc, pal, w, h, y in layers:
        half = w / 2
        poly = Polygon(
            [(cx - half, y), (cx + half, y), (cx + half * 0.72, y + h), (cx - half * 0.72, y + h)],
            closed=True, facecolor=pal["soft"], edgecolor=pal["main"], linewidth=2.5, zorder=2,
        )
        ax.add_patch(poly)
        ax.text(cx, y + h * 0.62, name_tr, ha="center", va="center", fontsize=11.5,
                fontweight="bold", color=pal["main"], zorder=3)
        ax.text(cx, y + h * 0.38, f"({name_en})", ha="center", va="center", fontsize=8.5, color=MUTED, zorder=3)
        ax.text(cx, y + h * 0.14, desc, ha="center", va="center", fontsize=8, color=SUB, zorder=3)

    # Değer oku
    ax.annotate("", xy=(6.0, 5.75), xytext=(6.0, 0.9),
                arrowprops=dict(arrowstyle="-|>", color="#94a3b8", lw=2.5, mutation_scale=14))
    ax.text(6.25, 3.3, "değer\nve\nanlam\nartar", ha="left", va="center", fontsize=9.5, color=MUTED, linespacing=1.35)

    # Sağ panel — örnek hikâye
    panel_x, panel_y, panel_w, panel_h = 6.55, 0.55, 3.55, 5.95
    _shadow_box(ax, (panel_x, panel_y), panel_w, panel_h, "#cbd5e1", radius=0.15)
    ax.text(panel_x + panel_w / 2, panel_y + panel_h - 0.35, "Somut örnek: hasta takibi",
            ha="center", fontsize=11, fontweight="bold", color=INK)

    steps = [
        ("1. Veri", "38.5", PALETTE["data"]["main"]),
        ("2. Enformasyon", "Ateş: 38.5 °C", PALETTE["info"]["main"]),
        ("3. Bilgi", "Enfeksiyon riski yüksek", PALETTE["know"]["main"]),
        ("4. Bilgelik", "Antibiyotik tedavisi başlat", PALETTE["wisdom"]["main"]),
    ]
    sy = panel_y + panel_h - 1.05
    for label, sample, color in steps:
        ax.plot([panel_x + 0.35, panel_x + 0.35], [sy - 0.55, sy], color=color, lw=3, solid_capstyle="round")
        ax.text(panel_x + 0.55, sy - 0.08, label, fontsize=9.5, fontweight="bold", color=color, va="top")
        ax.text(panel_x + 0.55, sy - 0.42, sample, fontsize=9, color=SUB, va="top")
        if label != "4. Bilgelik":
            ax.annotate("", xy=(panel_x + panel_w / 2, sy - 0.75), xytext=(panel_x + panel_w / 2, sy - 0.58),
                        arrowprops=dict(arrowstyle="-|>", color="#cbd5e1", lw=1.5))
        sy -= 1.35

    _save(fig, "hafta2_dikw_piramidi.png")


def veri_kavrami() -> None:
    """Veri kaynakları → işleme → içgörü boru hattı."""
    fig, ax = _setup((11, 5.8))
    ax.set_xlim(0, 11)
    ax.set_ylim(0, 5.8)

    ax.text(5.5, 5.35, "Veri Dünyasına Hoş Geldiniz", ha="center", fontsize=18, fontweight="bold", color=INK)
    ax.text(5.5, 4.95, "Ham kaynaklardan eyleme dönüştürülebilir içgörüye giden yol", ha="center", fontsize=10.5, color=MUTED)

    # Sol — kaynaklar
    ax.text(1.55, 4.35, "Veri kaynakları", ha="center", fontsize=11, fontweight="bold", color=INK)
    sources = [
        ("Sensörler", "IoT, sıcaklık", "#0891b2"),
        ("Web & API", "JSON, REST", "#2563eb"),
        ("Dosyalar", "CSV, Excel", "#059669"),
        ("Metin / Medya", "Tweet, video", "#d97706"),
    ]
    for i, (title, sub, color) in enumerate(sources):
        y = 3.55 - i * 0.82
        _label_block(ax, 0.35, y, 2.4, 0.68, title, sub, color)

    # Orta — işleme
    mid_x = 4.0
    ax.text(mid_x + 1.55, 4.35, "İşleme katmanı", ha="center", fontsize=11, fontweight="bold", color=INK)
    pipeline = [
        ("Toplama", "ETL / streaming"),
        ("Temizleme", "Eksik, aykırı değer"),
        ("Analiz", "Pandas, SQL, ML"),
    ]
    for i, (title, sub) in enumerate(pipeline):
        y = 3.35 - i * 0.95
        _label_block(ax, mid_x, y, 3.1, 0.78, title, sub, "#2563eb")

    # Sağ — çıktı
    ax.text(9.0, 4.35, "Değer / çıktı", ha="center", fontsize=11, fontweight="bold", color=INK)
    outputs = [
        ("Görselleştirme", "Grafik, dashboard"),
        ("Rapor", "KPI, tablo"),
        ("Karar", "Insight, aksiyon"),
    ]
    for i, (title, sub) in enumerate(outputs):
        y = 3.35 - i * 0.95
        _label_block(ax, 7.45, y, 3.1, 0.78, title, sub, "#7c3aed")

    # Oklar
    for y in (3.0, 2.05, 1.1):
        arrow = FancyArrowPatch((2.85, y + 0.34), (3.92, y + 0.34),
                                arrowstyle="-|>", mutation_scale=12, color="#94a3b8", lw=2)
        ax.add_patch(arrow)
        arrow2 = FancyArrowPatch((7.15, y + 0.34), (7.38, y + 0.34),
                                 arrowstyle="-|>", mutation_scale=12, color="#94a3b8", lw=2)
        ax.add_patch(arrow2)

    # Alt şerit — DIKW mini akış
    strip_y = 0.35
    ax.add_patch(FancyBboxPatch((0.4, strip_y), 10.2, 0.95, boxstyle="round,pad=0.02,rounding_size=0.12",
                                facecolor="#f8fafc", edgecolor="#e2e8f0", linewidth=1.5))
    ax.text(5.5, strip_y + 0.72, "Bu derste odak: ham veriyi toplamak, işlemek ve anlamlı sonuç üretmek",
            ha="center", fontsize=10, fontweight="bold", color=INK)
    mini = ["Veri", "Enformasyon", "Bilgi", "Bilgelik"]
    mini_colors = [PALETTE["data"]["main"], PALETTE["info"]["main"], PALETTE["know"]["main"], PALETTE["wisdom"]["main"]]
    xs = [2.0, 4.3, 6.6, 8.9]
    for i, (word, color) in enumerate(zip(mini, mini_colors)):
        circ = Circle((xs[i], strip_y + 0.28), 0.22, facecolor=color, edgecolor="white", linewidth=1.5, alpha=0.9)
        ax.add_patch(circ)
        ax.text(xs[i], strip_y + 0.28, str(i + 1), ha="center", va="center", fontsize=8, color="white", fontweight="bold")
        ax.text(xs[i], strip_y + 0.05, word, ha="center", fontsize=8.5, color=color, fontweight="bold")
        if i < 3:
            ax.annotate("", xy=(xs[i + 1] - 0.35, strip_y + 0.28), xytext=(xs[i] + 0.35, strip_y + 0.28),
                        arrowprops=dict(arrowstyle="-|>", color="#cbd5e1", lw=1.2))

    _save(fig, "hafta2_veri_kavrami.png")


def buyuk_veri_5v() -> None:
    """5 kartlı düzen — her V için kısa tanım ve örnek."""
    fig, ax = _setup((10.5, 6.2))
    ax.set_xlim(0, 10.5)
    ax.set_ylim(0, 6.2)

    ax.text(5.25, 5.75, "Büyük Verinin 5V'si", ha="center", fontsize=18, fontweight="bold", color=INK)
    ax.text(5.25, 5.32, "Geleneksel araçların yetmediği veri: hacim, hız, çeşitlilik, doğruluk ve değer bir arada",
            ha="center", fontsize=10, color=MUTED)

    cards = [
        ("Volume", "Hacim", "Veri miktarı çok büyük", "YouTube: dk'da 500 saat video", "#2563eb", "#dbeafe", 0.45, 3.35),
        ("Velocity", "Hız", "Üretim ve işleme hızı yüksek", "Borsa, dolandırıcılık tespiti", "#0891b2", "#cffafe", 3.55, 3.35),
        ("Variety", "Çeşitlilik", "Format ve kaynak çok", "Tablo + video + log + sensör", "#059669", "#d1fae5", 6.65, 3.35),
        ("Veracity", "Doğruluk", "Veri kalitesi kritik", "GIGO: çöp girer, çöp çıkar", "#d97706", "#fef3c7", 1.85, 1.15),
        ("Value", "Değer", "İş sonucu üretmeli", "Netflix: House of Cards kararı", "#7c3aed", "#ede9fe", 5.15, 1.15),
    ]

    for en, tr, desc, example, main, soft, x, y in cards:
        w, h = 2.85, 1.75
        # renkli üst şerit
        ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.02,rounding_size=0.14",
                                    facecolor="white", edgecolor=main, linewidth=2.2, zorder=2))
        ax.add_patch(FancyBboxPatch((x + 0.06, y + h - 0.52), w - 0.12, 0.46, boxstyle="round,pad=0.01,rounding_size=0.1",
                                    facecolor=soft, edgecolor="none", zorder=3))
        badge = Circle((x + 0.38, y + h - 0.28), 0.22, facecolor=main, edgecolor="white", linewidth=1.5, zorder=4)
        ax.add_patch(badge)
        ax.text(x + 0.38, y + h - 0.28, "V", ha="center", va="center", fontsize=10, fontweight="bold", color="white", zorder=5)
        ax.text(x + 0.72, y + h - 0.22, en, fontsize=11.5, fontweight="bold", color=main, va="center", zorder=4)
        ax.text(x + w - 0.12, y + h - 0.22, tr, fontsize=10, color=main, ha="right", va="center", zorder=4)
        ax.text(x + 0.18, y + h - 0.78, desc, fontsize=9.2, color=SUB, va="top", zorder=4)
        ax.text(x + 0.18, y + 0.22, f"Örn: {example}", fontsize=8.5, color=MUTED, style="italic", va="bottom", zorder=4)

    ax.text(5.25, 0.42,
            "Tek bilgisayar / Excel yetersiz kalır → Hadoop, Spark, Kafka ile dağıtık işleme",
            ha="center", fontsize=9.5, color=MUTED,
            bbox=dict(boxstyle="round,pad=0.45", facecolor="#f8fafc", edgecolor="#e2e8f0"))

    _save(fig, "hafta2_buyuk_veri_5v.png")


if __name__ == "__main__":
    dikw_piramidi()
    veri_kavrami()
    buyuk_veri_5v()
