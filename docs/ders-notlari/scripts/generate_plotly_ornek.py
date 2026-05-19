#!/usr/bin/env python3
"""Plotly benzeri scatter — statik PNG (matplotlib fallback)."""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

OUT = Path(__file__).resolve().parent.parent / "images" / "plotly_ornek.png"


def main() -> None:
    np.random.seed(42)
    df = pd.DataFrame({
        "aylik_harcama": np.round(np.random.uniform(50, 500, 150), 2),
        "destek_cagri": np.random.poisson(1.2, 150),
        "churn": np.random.choice(["Kaldı", "Ayrıldı"], 150, p=[0.72, 0.28]),
    })

    fig, ax = plt.subplots(figsize=(9, 5.5))
    colors = {"Kaldı": "#2563eb", "Ayrıldı": "#dc2626"}
    for label in ["Kaldı", "Ayrıldı"]:
        sub = df[df["churn"] == label]
        ax.scatter(sub["aylik_harcama"], sub["destek_cagri"],
                   alpha=0.65, s=40, c=colors[label], label=label, edgecolors="white", linewidth=0.3)

    ax.set_title("Plotly scatter örneği — harcama vs destek (churn renkli)", fontsize=12)
    ax.set_xlabel("Aylık harcama (TL)")
    ax.set_ylabel("Destek çağrısı sayısı")
    ax.legend(title="Churn")
    ax.grid(True, alpha=0.3)
    fig.text(0.5, 0.02, "Canlı sürümde Plotly ile zoom/hover/tooltip eklenir",
             ha="center", fontsize=9, color="#666")

    OUT.parent.mkdir(parents=True, exist_ok=True)
    plt.tight_layout(rect=[0, 0.04, 1, 1])
    plt.savefig(OUT, dpi=130, bbox_inches="tight")
    print(f"Kaydedildi: {OUT}")


if __name__ == "__main__":
    main()
