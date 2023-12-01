#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2024, Francisco Fernandez
# License: CC BY-SA 4.0
#   https://github.com/fernandezfran/thesis/blob/main/LICENSE
import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams.update({"font.size": 12})

fig, ax = plt.subplots()

for i, (experimento, m) in enumerate(zip(["litiad", "amorf"], ["^", "v"])):
    dataset = pd.read_csv(f"datasets/pdf-{experimento}a.csv")
    ax.scatter(
        dataset.r, dataset.gofr, color="k", marker=m, label=f"Si {experimento}o"
    )

    for metodo, c, ls, l in zip(
        ["cristal", "DFTB"],
        ["tab:orange", "tab:blue"],
        ["dashed", "solid"],
        ["cristalinas", "DFTB"],
    ):
        dataset = pd.read_csv(f"datasets/pdf-{experimento}a-{metodo}.csv")

        l = None if i == 0 else l
        ax.plot(dataset.r, dataset.gofr, color=c, ls=ls, label=l)

ax.set_xlim((2.1, 5.5))
ax.set_xlabel(r"r ($\AA$)")

ax.set_ylabel(r"G(r) ($\AA^{-2}$)")

ax.legend()

fig.tight_layout()
fig.savefig("pdfs.png", dpi=600)
