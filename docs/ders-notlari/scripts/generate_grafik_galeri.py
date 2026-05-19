#!/usr/bin/env python3
"""12 grafik türü galerisi + ek 4 grafik."""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

OUT = Path(__file__).resolve().parent.parent / "images"


def make_df():
    np.random.seed(42)
    df = pd.DataFrame({
        "tarih": pd.date_range("2025-01-01", periods=120, freq="D"),
        "satis": np.random.randint(80, 220, 120) + np.sin(np.linspace(0, 6, 120)) * 30,
        "sehir": np.random.choice(["Ankara", "İstanbul", "İzmir"], 120),
        "kanal": np.random.choice(["Web", "Mobil", "Mağaza"], 120),
        "yas": np.random.randint(18, 65, 120),
        "harcama": np.random.uniform(50, 500, 120),
    })
    df["ay"] = df["tarih"].dt.to_period("M").astype(str)
    return df


def gallery_main():
    df = make_df()
    aylik = df.groupby("ay")["satis"].sum()

    fig, axes = plt.subplots(4, 3, figsize=(16, 18))
    fig.suptitle("Grafik türleri galerisi (1/2) — 12 tür", fontsize=14, y=1.005)

    axes[0, 0].hist(df["yas"], bins=12, color="#6366f1", edgecolor="white")
    axes[0, 0].set_title("1) Histogram")

    sehir_cnt = df["sehir"].value_counts()
    axes[0, 1].bar(sehir_cnt.index, sehir_cnt.values, color="#16a34a")
    axes[0, 1].set_title("2) Bar")
    axes[0, 1].tick_params(axis="x", rotation=15)

    axes[0, 2].scatter(df["yas"], df["harcama"], alpha=0.5, c="#dc2626", s=25)
    axes[0, 2].set_title("3) Scatter")

    axes[1, 0].plot(aylik.index, aylik.values, marker="o", color="#2563eb")
    axes[1, 0].set_title("4) Line (zaman)")
    axes[1, 0].tick_params(axis="x", rotation=30)

    sns.boxplot(data=df, x="kanal", y="harcama", ax=axes[1, 1], hue="kanal", legend=False,
                palette=["#6366f1", "#16a34a", "#f59e0b"])
    axes[1, 1].set_title("5) Boxplot")

    sns.heatmap(df[["satis", "yas", "harcama"]].corr(), annot=True, ax=axes[1, 2],
                cmap="RdBu_r", center=0, fmt=".2f")
    axes[1, 2].set_title("6) Heatmap")

    sns.countplot(data=df, x="sehir", hue="kanal", ax=axes[2, 0])
    axes[2, 0].set_title("7) Countplot")
    axes[2, 0].tick_params(axis="x", rotation=15)

    sns.kdeplot(data=df, x="harcama", hue="sehir", ax=axes[2, 1], fill=True, alpha=0.3)
    axes[2, 1].set_title("8) KDE")

    sns.violinplot(data=df, x="kanal", y="harcama", ax=axes[2, 2], hue="kanal", legend=False,
                   palette="pastel")
    axes[2, 2].set_title("9) Violin")

    kanal_pay = df["kanal"].value_counts()
    axes[3, 0].pie(kanal_pay.values, labels=kanal_pay.index, autopct="%1.0f%%")
    axes[3, 0].set_title("10) Pasta")

    pivot = df.groupby(["ay", "kanal"])["satis"].sum().unstack(fill_value=0)
    pivot.plot(kind="bar", stacked=True, ax=axes[3, 1], colormap="Set2")
    axes[3, 1].set_title("11) Yığılmış bar")
    axes[3, 1].tick_params(axis="x", rotation=30)
    axes[3, 1].legend(fontsize=7)

    sns.stripplot(data=df, x="sehir", y="harcama", ax=axes[3, 2], alpha=0.5, jitter=0.25)
    axes[3, 2].set_title("12) Stripplot")
    axes[3, 2].tick_params(axis="x", rotation=15)

    plt.tight_layout()
    path = OUT / "grafik_galeri.png"
    plt.savefig(path, dpi=125, bbox_inches="tight")
    plt.close()
    print(f"Kaydedildi: {path}")


def gallery_extra():
    df = make_df()
    fig, axes = plt.subplots(2, 2, figsize=(12, 9))
    fig.suptitle("Grafik türleri galerisi (2/2) — ek 4 tür", fontsize=13)

    # Area chart
    daily = df.groupby("tarih")["satis"].sum().reset_index()
    axes[0, 0].fill_between(daily["tarih"], daily["satis"], alpha=0.4, color="#2563eb")
    axes[0, 0].plot(daily["tarih"], daily["satis"], color="#2563eb", linewidth=1)
    axes[0, 0].set_title("13) Area (alan) — zaman trendi")
    axes[0, 0].tick_params(axis="x", rotation=30)

    # Hexbin — çok nokta
    np.random.seed(0)
    x = np.random.randn(3000)
    y = x * 0.5 + np.random.randn(3000) * 0.8
    axes[0, 1].hexbin(x, y, gridsize=25, cmap="YlOrRd", mincnt=1)
    axes[0, 1].set_title("14) Hexbin — çok nokta")

    # Horizontal bar
    sehir_avg = df.groupby("sehir")["harcama"].mean().sort_values()
    axes[1, 0].barh(sehir_avg.index, sehir_avg.values, color="#16a34a")
    axes[1, 0].set_title("15) Yatay bar")

    # Hist + KDE — aynı y-ekseni: yoğunluk (density). count + kde karışınca eğri yanıltıcı görünür.
    sns.histplot(
        df["harcama"], bins=14, stat="density", kde=True,
        color="#6366f1", edgecolor="white", linewidth=0.6,
        line_kws={"color": "#dc2626", "linewidth": 2},
        ax=axes[1, 1],
    )
    axes[1, 1].set_xlabel("Harcama (TL)")
    axes[1, 1].set_ylabel("Yoğunluk")
    axes[1, 1].set_title("16) Histogram + KDE (density)")

    plt.tight_layout()
    path = OUT / "grafik_galeri_ek.png"
    plt.savefig(path, dpi=125, bbox_inches="tight")
    plt.close()
    print(f"Kaydedildi: {path}")


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    gallery_main()
    gallery_extra()


if __name__ == "__main__":
    main()
