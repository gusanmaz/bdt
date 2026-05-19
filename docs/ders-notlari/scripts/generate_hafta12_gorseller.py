#!/usr/bin/env python3
"""Hafta 1 ders notları için yerel görseller üretir.

Hafta 2 görselleri için: scripts/generate_hafta2_gorseller.py
"""
from pathlib import Path

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch

OUT = Path(__file__).resolve().parent.parent / "images"
OUT.mkdir(parents=True, exist_ok=True)


def save(fig, name: str) -> None:
    path = OUT / name
    fig.savefig(path, dpi=140, bbox_inches="tight", facecolor=fig.get_facecolor())
    plt.close(fig)
    print("wrote", path)


def dikw_piramidi():
    fig, ax = plt.subplots(figsize=(8, 6))
    fig.patch.set_facecolor("#f8fafc")
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis("off")

    layers = [
        ("BİLGELİK (Wisdom)", "Doğru zamanda doğru karar", "#7c3aed", 2.0, 8.2, 6.0, 1.2),
        ("BİLGİ (Knowledge)", "Deneyim + yorum", "#2563eb", 2.8, 6.5, 4.4, 1.2),
        ("ENFORMASYON (Information)", "Bağlam eklenmiş veri", "#0891b2", 3.6, 4.8, 2.8, 1.2),
        ("VERİ (Data)", "Ham ölçüm / gözlem", "#64748b", 4.4, 3.1, 1.2, 1.2),
    ]
    for title, sub, color, x, y, w, h in layers:
        box = FancyBboxPatch(
            (x, y), w, h,
            boxstyle="round,pad=0.02,rounding_size=0.08",
            linewidth=1.5, edgecolor=color, facecolor="white", alpha=0.95,
        )
        ax.add_patch(box)
        ax.text(x + w / 2, y + h * 0.62, title, ha="center", va="center", fontsize=11, fontweight="bold", color=color)
        ax.text(x + w / 2, y + h * 0.28, sub, ha="center", va="center", fontsize=9, color="#334155")

    ax.text(5, 9.5, "DIKW Piramidi — Veriden bilgeliğe", ha="center", fontsize=14, fontweight="bold", color="#0f172a")
    ax.annotate("", xy=(9.2, 3.5), xytext=(9.2, 9.0), arrowprops=dict(arrowstyle="->", color="#94a3b8", lw=2))
    ax.text(9.45, 6.2, "değer\nartar", fontsize=9, color="#64748b", rotation=90, va="center")
    save(fig, "hafta2_dikw_piramidi.png")


def veri_kavrami():
    fig, ax = plt.subplots(figsize=(9, 4.5))
    fig.patch.set_facecolor("#f8fafc")
    ax.set_xlim(0, 9)
    ax.set_ylim(0, 4.5)
    ax.axis("off")
    ax.text(4.5, 4.1, "Veri dünyasına hoş geldiniz!", ha="center", fontsize=15, fontweight="bold", color="#0f172a")

    boxes = [
        ("38.5", "Tek başına\nanlamsız sayı", "#94a3b8", 0.4, 1.2),
        ("→", "", "#cbd5e1", 2.0, 1.8),
        ("38.5°C", "Hasta ateşi\n(enformasyon)", "#0891b2", 2.5, 1.2),
        ("→", "", "#cbd5e1", 4.8, 1.8),
        ("Antibiyotik?", "Klinik karar\n(bilgelik)", "#7c3aed", 5.3, 1.2),
    ]
    for item in boxes:
        if item[0] == "→":
            ax.text(item[3], item[4], "→", fontsize=28, color="#64748b")
            continue
        txt, sub, color, x, y = item
        box = FancyBboxPatch((x, y), 1.8, 1.6, boxstyle="round,pad=0.02", edgecolor=color, facecolor="white", lw=1.5)
        ax.add_patch(box)
        ax.text(x + 0.9, y + 1.05, txt, ha="center", fontsize=13, fontweight="bold", color=color)
        ax.text(x + 0.9, y + 0.45, sub, ha="center", fontsize=8.5, color="#475569")

    ax.text(4.5, 0.35, "Büyük Veri dersinde ham veriyi anlamlı içgörüye dönüştürmeyi öğreneceğiz.", ha="center", fontsize=10, color="#475569")
    save(fig, "hafta2_veri_kavrami.png")


def mapreduce_akisi():
    fig, ax = plt.subplots(figsize=(10, 3.2))
    fig.patch.set_facecolor("#f8fafc")
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 3.2)
    ax.axis("off")
    steps = [
        ("SPLIT", "Metni satırlara böl", "#64748b"),
        ("MAP", "(kelime, 1) üret", "#2563eb"),
        ("SHUFFLE", "Aynı kelimeleri grupla", "#0891b2"),
        ("REDUCE", "Sayıları topla", "#7c3aed"),
    ]
    w = 2.0
    for i, (title, sub, color) in enumerate(steps):
        x = 0.4 + i * 2.4
        box = FancyBboxPatch((x, 0.9), w, 1.5, boxstyle="round,pad=0.02", edgecolor=color, facecolor="white", lw=2)
        ax.add_patch(box)
        ax.text(x + w / 2, 1.85, title, ha="center", fontweight="bold", color=color, fontsize=12)
        ax.text(x + w / 2, 1.35, sub, ha="center", fontsize=8.5, color="#475569")
        if i < len(steps) - 1:
            ax.annotate("", xy=(x + w + 0.15, 1.65), xytext=(x + w + 0.05, 1.65),
                        arrowprops=dict(arrowstyle="->", color="#94a3b8", lw=2))
    ax.text(5, 2.85, "Word Count — MapReduce akışı (Python simülasyonu)", ha="center", fontsize=13, fontweight="bold")
    save(fig, "hafta1_mapreduce_akisi.png")


def bes_v_gorsel():
    fig, ax = plt.subplots(figsize=(9, 5))
    fig.patch.set_facecolor("#f8fafc")
    ax.axis("off")
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.text(5, 5.5, "Büyük Verinin 5V'si", ha="center", fontsize=14, fontweight="bold")

    items = [
        ("Volume\nHacim", "Çok büyük", "#2563eb", 1.0, 3.2),
        ("Velocity\nHız", "Çok hızlı", "#0891b2", 3.0, 3.2),
        ("Variety\nÇeşitlilik", "Çok format", "#059669", 5.0, 3.2),
        ("Veracity\nDoğruluk", "Güvenilirlik", "#d97706", 2.0, 1.0),
        ("Value\nDeğer", "İş değeri", "#7c3aed", 4.0, 1.0),
    ]
    for title, sub, color, x, y in items:
        circ = plt.Circle((x, y), 0.85, color=color, alpha=0.15)
        ax.add_patch(circ)
        ax.add_patch(plt.Circle((x, y), 0.85, fill=False, edgecolor=color, lw=2))
        ax.text(x, y + 0.15, title, ha="center", va="center", fontsize=9, fontweight="bold", color=color)
        ax.text(x, y - 0.45, sub, ha="center", fontsize=8, color="#475569")
    save(fig, "hafta2_buyuk_veri_5v.png")


if __name__ == "__main__":
    mapreduce_akisi()
