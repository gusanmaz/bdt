#!/usr/bin/env python3
"""Seaborn örnek grafikleri — hafta6 Bölüm 4."""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

OUT = Path(__file__).resolve().parent.parent / "images" / "seaborn_ornek.png"


def main() -> None:
    np.random.seed(42)
    df = pd.DataFrame({
        "yas": np.random.randint(18, 65, 200),
        "aylik_harcama": np.round(np.random.uniform(50, 500, 200), 2),
        "sehir": np.random.choice(["Ankara", "İstanbul", "İzmir", "Bursa"], 200),
        "destek_cagri": np.random.poisson(1.2, 200),
        "churn": np.random.choice([0, 1], 200, p=[0.72, 0.28]),
    })
    df["churn_etiket"] = df["churn"].map({0: "Kaldı", 1: "Ayrıldı"})

    sns.set_theme(style="whitegrid", font_scale=0.95)
    fig, axes = plt.subplots(2, 2, figsize=(12, 9))
    fig.suptitle("Seaborn örnekleri — countplot, boxplot, heatmap, violin", fontsize=13)

    sns.countplot(data=df, x="sehir", hue="churn_etiket", ax=axes[0, 0])
    axes[0, 0].set_title("Countplot — şehir × churn")
    axes[0, 0].tick_params(axis="x", rotation=25)

    sns.boxplot(data=df, x="churn_etiket", y="aylik_harcama", ax=axes[0, 1])
    axes[0, 1].set_title("Boxplot — churn vs harcama")

    num = df[["yas", "aylik_harcama", "destek_cagri", "churn"]]
    sns.heatmap(num.corr(), annot=True, ax=axes[1, 0], cmap="RdBu_r", center=0, fmt=".2f")
    axes[1, 0].set_title("Heatmap — korelasyon")

    sns.violinplot(data=df, x="churn_etiket", y="destek_cagri", ax=axes[1, 1])
    axes[1, 1].set_title("Violin — destek çağrısı dağılımı")

    plt.tight_layout()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(OUT, dpi=130, bbox_inches="tight")
    print(f"Kaydedildi: {OUT}")


if __name__ == "__main__":
    main()
