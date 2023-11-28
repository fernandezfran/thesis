#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2024, Francisco Fernandez
# License: CC BY-SA 4.0
#   https://github.com/fernandezfran/thesis/blob/main/LICENSE
import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams.update({"font.size": 12})

fig, ax = plt.subplots()

# picos cristalinos
_ = [
    ax.axvline(xpeak, color="tab:gray", linestyle="--", alpha=0.5 - 0.1 * i)
    for i, xpeak in enumerate((2.37, 3.87, 4.53), start=1)
]

# experimental
experimental = pd.read_csv("datos/rdf-experimental.csv")
plt.plot(
    experimental.r,
    experimental.rdf,
    marker="s",
    c="k",
    ls=":",
    label="datos experimentales",
)

# annealings con exnfriamiento exponencial
labels = ["ReaxFF", "DFTB conjunto A", "DFTB conjunto B"]
parametrizaciones = ["reax", "A", "B"]
colores = ["tab:orange", "tab:blue", "tab:green"]
for color, label, param in zip(colores, labels, parametrizaciones):
    df = pd.read_csv(f"datos/rdf-{param}.csv")
    ax.plot(df.r, df.rdf, color=color, label=label)

ax.set_xlabel(r"r [$\AA$]")
ax.set_ylabel("RDF Si-Si")
ax.set_xlim((1.5, 5))
ax.legend()
fig.savefig("rdf-curva.png", dpi=600)
plt.show()
