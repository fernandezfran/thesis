#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2024, Francisco Fernandez
# License: CC BY-SA 4.0
#   https://github.com/fernandezfran/thesis/blob/main/LICENSE
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

plt.rcParams.update({"font.size": 10})

fig, axes = plt.subplots(3, 3, sharex=True, sharey=True)

X_vals = [[0.21, 0.62, 1.25], [1.71, 2.17, 2.71], [3.25, 3.75, 4.2]]
names = ["r", "g0", "g1", "g2", "g3", "g4", "g+5"]
mask = names[1:]

for xvals, axis in zip(X_vals, axes):
    for x, ax in zip(xvals, axis):
        dataset = pd.read_csv(
            f"datasets/rdf/{x}.dat", delimiter="\s+", comment="#", names=names
        )

        for conectores in [0, 1, 2, 3, 4, "+5"]:
            ax.plot(dataset.r, dataset[f"g{conectores}"], label=conectores)

        ax.plot(dataset.r, dataset[mask].sum(axis=1), color="k", label="total")

        ax.text(6, 1.55, f"x = {x}")

        ax.set_xlim((4, 8))

        ax.set_ylim((0.0, 1.75))
        ax.grid(axis="y", linestyle=":")

axes[0][2].legend(title="conexiones", bbox_to_anchor=(1.05, 1.05), prop={"size": 8})

fig.text(0.5, 0.005, r"r [$\AA$]", ha="center")
fig.text(0.005, 0.5, "RDF Si-Li", va="center", rotation="vertical")

fig.subplots_adjust(wspace=0.1, hspace=0.1)

fig.tight_layout()
fig.savefig("interconexiones.png", dpi=600)
