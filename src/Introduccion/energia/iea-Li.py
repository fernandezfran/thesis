#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2024, Francisco Fernandez
# License: CC BY-SA 4.0
#   https://github.com/fernandezfran/thesis/blob/main/LICENSE
import matplotlib.pyplot as plt
import pandas as pd

df = pd.DataFrame(
    {
        "year": [2022, 2025, 2030, 2035, 2040, 2045, 2050],
        "ev": [69.8, 145.3, 349.5, 671.3, 907.1, 1005.7, 1039.5],
        "es": [3.85, 7.68, 18.5, 30.47, 44.89, 47.78, 49.68],
        "ed": [57.0, 74.0, 83.0, 92.0, 101.0, 111.0, 120.0],
    }
)

print((df["ev"] + df["es"] + df["ed"]).pct_change())

categorias = [
    "Vehículos eléctricos",
    "Almacenamientos estacionarios",
    "Otras aplicaciones",
]
heights = [df["ev"], df["es"], df["ed"]]

fig, ax = plt.subplots()

ax.bar(df["year"], heights[0], label=categorias[0], width=1.5)
for i in range(1, len(categorias)):
    ax.bar(df["year"], heights[i], width=1.5, bottom=sum(heights[:i]), label=categorias[i])

ax.set_xticks(df["year"])
ax.set_xlabel("Año")
ax.set_ylabel("Demanda total de litio (kt)")
ax.legend()

fig.tight_layout()
fig.savefig("iea-Li.png", dpi=600)
plt.show()
