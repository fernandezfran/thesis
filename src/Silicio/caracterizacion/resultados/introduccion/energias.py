#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2024, Francisco Fernandez
# License: CC BY-SA 4.0
#   https://github.com/fernandezfran/thesis/blob/main/LICENSE
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter
import numpy as np
import pandas as pd

plt.rcParams.update({"font.size": 10})

colors = ["tab:green", "tab:blue", "tab:orange", "tab:red"]
alfas = [0.2, 0.4, 0.6, 0.8]
X_vals = [[0.21, 0.62, 1.25], [1.71, 2.17, 2.71], [3.25, 3.75, 4.2]]
Anchos = [[0.002, 0.001, 0.0009], [0.0009, 0.0009, 0.0009], [0.0009, 0.0009, 0.0009]]
names = ["bins"] + [0.2, 0.4, 0.6, 0.8]

fig, axes = plt.subplots(3, 3, sharey="row")

for xvals, axis, anchos in zip(X_vals, axes, Anchos):
    for x, ax, ancho in zip(xvals, axis, anchos):
        dataset = pd.read_csv(
            f"datasets/{x}-histo.dat", delimiter=" ", comment="#", names=names
        )

        for alfa, color in zip(alfas, colors):
            ax.bar(
                dataset["bins"],
                dataset[alfa],
                width=ancho,
                color=color,
                alpha=0.75,
                label=alfa,
            )

        ax.text(0.1, 1.02, f"x = {x}", transform=ax.transAxes)

        ax.grid(axis="x", linestyle=":")
        ax.set_ylim((0.0, 0.3))

        ax.xaxis.set_major_formatter(FormatStrFormatter("%.2f"))

for i, (x, ancho) in enumerate(zip([0.21, 2.17, 4.2], [0.002, 0.0009, 0.0009])):
    dataset = pd.read_csv(
        f"datasets/md/{x}.dat", delimiter="\s+", comment="#", names=["bins", "freq"]
    )
    print(dataset)
    axes[i][i].bar(
        dataset["bins"],
        dataset["freq"],
        width=ancho,
        color="tab:gray",
        alpha=0.75,
        label="1.0",
    )

axes[2][2].legend(title=r"$\alpha$", bbox_to_anchor=(1.04, 1), prop={"size": 8})

fig.text(0.5, 0.005, "E / N (eV)", ha="center")
fig.text(0.005, 0.5, "frecuencias", va="center", rotation="vertical")

fig.subplots_adjust(wspace=0.05, hspace=0.25)
fig.tight_layout()

fig.savefig("energias.png", dpi=600)
