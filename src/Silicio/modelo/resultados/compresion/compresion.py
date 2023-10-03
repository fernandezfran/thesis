#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams.update({"font.size": 12})

colores = [
    "tab:green",
    "tab:red",
    "tab:orange",
    "tab:pink",
    "tab:purple",
    "tab:cyan",
    "tab:blue",
]
cristales = ["Li", "Li15Si4", "Li13Si4", "Li7Si3", "Li12Si7", "LiSi", "Si"]

fig, ax = plt.subplots()

for color, cristal in zip(colores, cristales):
    df = pd.read_csv(f"datos/{cristal}.csv")

    ax.plot(df.cf, df.dft, color=color, label=cristal)
    ax.scatter(df.cf, df.dftba, marker="^", color=color)
    ax.scatter(df.cf, df.dftbb, marker="v", color=color)

ax.set_xlim((0.68, 1.48))
ax.set_xlabel("Factor de compresión")
ax.set_ylim((-6, 2))
ax.set_ylabel("Energía (eV)")

ax.legend(ncol=3)

fig.tight_layout()
fig.savefig("compresion.png", dpi=600)
