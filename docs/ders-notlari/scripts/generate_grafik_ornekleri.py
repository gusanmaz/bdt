#!/usr/bin/env python3
"""Bölüm 6 eğitim görselleri — grafik okuma + ML kavramları."""
from pathlib import Path

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.linear_model import LinearRegression
from sklearn.metrics import confusion_matrix

OUT_DIR = Path(__file__).resolve().parent.parent / "images"
OUT_DIR.mkdir(parents=True, exist_ok=True)


def save(fig, name: str) -> None:
    path = OUT_DIR / name
    fig.savefig(path, dpi=140, bbox_inches="tight")
    plt.close(fig)
    print(f"  {path.name}")


def grafik_histogram_vs_kde():
    """Histogram + KDE — açıklamalar altta, üst üste binmez."""
    np.random.seed(42)
    yas = np.concatenate([np.random.normal(28, 5, 120), np.random.normal(45, 7, 80)])

    fig, axes = plt.subplots(1, 2, figsize=(11, 4.8))
    fig.suptitle("Histogram vs KDE — aynı veri, farklı gösterim", fontsize=12, y=1.02)

    axes[0].hist(yas, bins=14, color="#6366f1", edgecolor="white", alpha=0.88)
    axes[0].set_title("Histogram")
    axes[0].set_xlabel("Yaş")
    axes[0].set_ylabel("Kişi sayısı (frekans)")
    axes[0].text(0.03, 0.04,
                 "Her sütun = bir yaş aralığı.\nYükseklik = o aralıktaki kişi sayısı.",
                 transform=axes[0].transAxes, fontsize=8.5, va="bottom",
                 bbox=dict(boxstyle="round,pad=0.4", fc="#eef2ff", ec="#6366f1", alpha=0.95))

    sns.kdeplot(x=yas, ax=axes[1], fill=True, color="#16a34a", alpha=0.35, linewidth=2)
    axes[1].set_title("KDE (yoğunluk eğrisi)")
    axes[1].set_xlabel("Yaş")
    axes[1].set_ylabel("Yoğunluk")
    axes[1].text(0.03, 0.04,
                 "Eğri yüksekliği = o bölgede\nveri yoğunluğu (göreli sıklık).",
                 transform=axes[1].transAxes, fontsize=8.5, va="bottom",
                 bbox=dict(boxstyle="round,pad=0.4", fc="#ecfdf5", ec="#16a34a", alpha=0.95))

    plt.tight_layout(rect=[0, 0, 1, 0.96])
    save(fig, "grafik_histogram_kde.png")


def grafik_boxplot_aciklama():
    """Şematik boxplot — alt bölümde not + mini örnek ayrı panellerde."""
    fig = plt.figure(figsize=(10, 7.2))

    ax = fig.add_axes([0.06, 0.40, 0.88, 0.56])
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis("off")
    ax.set_title("Boxplot anatomisi — parçaları tanıyalım", fontsize=13, fontweight="bold", pad=10)

    cx = 4.2
    wmin, q1, med, q3, wmax = 1.8, 3.5, 5.0, 6.5, 8.2
    outlier_y = 9.2

    ax.plot([cx, cx], [wmin, q1], color="#475569", linewidth=2)
    ax.plot([cx, cx], [q3, wmax], color="#475569", linewidth=2)
    ax.plot([cx - 0.35, cx + 0.35], [wmin, wmin], color="#475569", linewidth=2)
    ax.plot([cx - 0.35, cx + 0.35], [wmax, wmax], color="#475569", linewidth=2)
    ax.add_patch(mpatches.Rectangle((cx - 0.55, q1), 1.1, q3 - q1,
                                    facecolor="#dbeafe", edgecolor="#2563eb", linewidth=2))
    ax.plot([cx - 0.55, cx + 0.55], [med, med], color="#dc2626", linewidth=3)
    ax.scatter([cx], [outlier_y], s=80, c="#dc2626", zorder=5, edgecolors="white")

    labels = [
        (outlier_y, "Aykırı değer (outlier)\nNormal aralığın dışında tek nokta"),
        (wmax, "Üst bıyık ucu = max (aykırı hariç)"),
        (q3, "Q3 — üst çeyrek (%75 altında kalan sınır)"),
        (med, "Medyan — ortadaki kırmızı çizgi (%50)"),
        (q1, "Q1 — alt çeyrek (%25)"),
        (wmin, "Alt bıyık ucu = min (aykırı hariç)"),
    ]
    for y, text in labels:
        ax.annotate("", xy=(cx + 0.6, y), xytext=(6.6, y),
                    arrowprops=dict(arrowstyle="-", color="#64748b", lw=1.2))
        fw = "bold" if "Medyan" in text else "normal"
        ax.text(6.65, y, text, va="center", fontsize=9, fontweight=fw)

    ax_note = fig.add_axes([0.06, 0.05, 0.44, 0.28])
    ax_note.axis("off")
    ax_note.text(
        0.5, 0.5,
        "Kutu (Q1–Q3) = orta %50'lik dilim.\n"
        "Kutu dışındaki noktalar genelde IQR kuralına göre aykırı sayılır.",
        ha="center", va="center", fontsize=9.5, wrap=True,
        bbox=dict(boxstyle="round,pad=0.55", fc="#fef9c3", ec="#ca8a04", alpha=0.95),
        transform=ax_note.transAxes,
    )

    np.random.seed(3)
    sample = np.concatenate([np.random.normal(200, 40, 40), [520]])
    ax_in = fig.add_axes([0.54, 0.06, 0.40, 0.26])
    ax_in.boxplot(sample, vert=True, patch_artist=True,
                  boxprops=dict(facecolor="#dbeafe"),
                  medianprops=dict(color="#dc2626", linewidth=2))
    ax_in.set_title("Mini gerçek veri örneği", fontsize=9)
    ax_in.set_xticks([])
    ax_in.set_ylabel("TL", fontsize=8)

    save(fig, "grafik_boxplot_aciklama.png")


def grafik_scatter_korelasyon():
    np.random.seed(99)
    n = 150
    destek = np.random.poisson(1.5, n)
    harcama = 180 + destek * 45 + np.random.normal(0, 40, n)
    fig, axes = plt.subplots(1, 2, figsize=(11, 4.5))
    fig.suptitle("Scatter plot — ilişki ve korelasyon", fontsize=12)

    axes[0].scatter(destek, harcama, alpha=0.55, c="#6366f1")
    axes[0].set_xlabel("Destek çağrısı sayısı")
    axes[0].set_ylabel("Aylık harcama (TL)")
    axes[0].set_title("Pozitif ilişki")
    z = np.polyfit(destek, harcama, 1)
    xs = np.linspace(destek.min(), destek.max(), 50)
    axes[0].plot(xs, np.poly1d(z)(xs), "r--", linewidth=2, label="Trend")
    axes[0].legend(fontsize=8)

    r = np.corrcoef(destek, harcama)[0, 1]
    axes[1].scatter(destek, np.random.uniform(50, 500, n), alpha=0.55, c="#94a3b8")
    axes[1].set_xlabel("Destek çağrısı")
    axes[1].set_ylabel("Rastgele skor")
    axes[1].set_title(f"İlişki yok  (sol: r ≈ {r:.2f})")
    plt.tight_layout()
    save(fig, "grafik_scatter_korelasyon.png")


def grafik_bar_vs_pie():
    labels = ["Web", "Mobil", "Mağaza"]
    vals = [45, 38, 17]
    fig, axes = plt.subplots(1, 2, figsize=(10, 4.5))
    fig.suptitle("Bar vs Pasta", fontsize=12)
    axes[0].bar(labels, vals, color=["#2563eb", "#16a34a", "#f59e0b"])
    axes[0].set_ylabel("Pay (%)")
    for i, v in enumerate(vals):
        axes[0].text(i, v + 1, f"%{v}", ha="center")
    axes[1].pie(vals, labels=labels, autopct="%1.0f%%", colors=["#2563eb", "#16a34a", "#f59e0b"])
    plt.tight_layout()
    save(fig, "grafik_bar_vs_pie.png")


def ml_regression_gorsel():
    np.random.seed(42)
    yas = np.random.randint(20, 60, 120)
    destek = np.random.poisson(1.2, 120)
    harcama = 50 + 2.5 * yas + 30 * destek + np.random.normal(0, 40, 120)
    fig, ax = plt.subplots(figsize=(8, 5))
    sc = ax.scatter(yas, harcama, c=destek, cmap="viridis", alpha=0.65, edgecolors="white")
    plt.colorbar(sc, label="Destek çağrısı")
    ax.set_xlabel("Yaş")
    ax.set_ylabel("Aylık harcama (TL)")
    ax.set_title("Regresyon — model bir formül arar")
    ax.text(0.03, 0.04, "tahmin = sabit + a×yaş + b×destek",
            transform=ax.transAxes, fontsize=9, va="bottom",
            bbox=dict(boxstyle="round", fc="#fef9c3", alpha=0.95))
    plt.tight_layout()
    save(fig, "ml_regression_gorsel.png")


def ml_confusion_matrix():
    np.random.seed(1)
    y_true = np.random.choice([0, 1], 100, p=[0.7, 0.3])
    y_pred = y_true.copy()
    flip = np.random.choice(100, 25, replace=False)
    y_pred[flip] = 1 - y_pred[flip]
    cm = confusion_matrix(y_true, y_pred)
    fig, ax = plt.subplots(figsize=(6.5, 5.5))
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", ax=ax,
                xticklabels=["Tahmin: Kaldı", "Tahmin: Ayrıldı"],
                yticklabels=["Gerçek: Kaldı", "Gerçek: Ayrıldı"])
    ax.set_title("Confusion Matrix\nSatır = gerçek, sütun = tahmin")
    plt.tight_layout()
    save(fig, "ml_confusion_matrix.png")


def ml_karar_agaci_kavram():
    fig, ax = plt.subplots(figsize=(9.5, 5.2))
    ax.set_xlim(0.2, 9.8)
    ax.set_ylim(0.2, 6)
    ax.axis("off")
    ax.set_title("Karar ağacı — soru sorarak böl", fontsize=12)
    boxes = [
        (4.9, 5, "Harcama > 250 TL?", "#dbeafe"),
        (2.6, 3, "Destek ≥ 3?", "#dcfce7"),
        (7.2, 3, "Yaş > 40?", "#dcfce7"),
        (1.7, 1, "Ayrıldı", "#fecaca"),
        (3.5, 1, "Kaldı", "#bbf7d0"),
        (6.4, 1, "Kaldı", "#bbf7d0"),
        (8.2, 1, "Ayrıldı", "#fecaca"),
    ]
    for x, y, text, color in boxes:
        ax.add_patch(mpatches.FancyBboxPatch((x - 1.1, y - 0.35), 2.2, 0.7,
                     boxstyle="round,pad=0.02", fc=color, ec="#64748b"))
        ax.text(x, y, text, ha="center", va="center", fontsize=9)
    for x1, y1, x2, y2, label in [
        (4.9, 4.65, 2.6, 3.35, "Evet"), (4.9, 4.65, 7.2, 3.35, "Hayır"),
        (2.6, 2.65, 1.7, 1.35, "Evet"), (2.6, 2.65, 3.5, 1.35, "Hayır"),
        (7.2, 2.65, 6.4, 1.35, "Hayır"), (7.2, 2.65, 8.2, 1.35, "Evet"),
    ]:
        ax.annotate("", xy=(x2, y2), xytext=(x1, y1),
                    arrowprops=dict(arrowstyle="->", color="#475569"))
        ax.text((x1 + x2) / 2, (y1 + y2) / 2, label, fontsize=7, color="#475569")
    plt.tight_layout()
    save(fig, "ml_karar_agaci_kavram.png")


def ml_kmeans_gorsel():
    np.random.seed(42)
    X = np.vstack([
        np.random.normal([2, 2], 0.6, (60, 2)),
        np.random.normal([6, 6], 0.7, (60, 2)),
        np.random.normal([6, 2], 0.5, (50, 2)),
    ])
    km = KMeans(n_clusters=3, random_state=42, n_init=10).fit(X)
    fig, ax = plt.subplots(figsize=(7, 5))
    ax.scatter(X[:, 0], X[:, 1], c=km.labels_, cmap="Set2", alpha=0.7, edgecolors="white")
    ax.scatter(km.cluster_centers_[:, 0], km.cluster_centers_[:, 1],
               c="black", marker="X", s=120, label="Merkezler")
    ax.set_title("KMeans — benzer noktalar aynı gruba")
    ax.legend()
    plt.tight_layout()
    save(fig, "ml_kmeans_gorsel.png")


def main():
    print("Görseller üretiliyor...")
    grafik_histogram_vs_kde()
    grafik_boxplot_aciklama()
    grafik_scatter_korelasyon()
    grafik_bar_vs_pie()
    ml_regression_gorsel()
    ml_confusion_matrix()
    ml_karar_agaci_kavram()
    ml_kmeans_gorsel()
    print("Tamam.")


if __name__ == "__main__":
    main()
