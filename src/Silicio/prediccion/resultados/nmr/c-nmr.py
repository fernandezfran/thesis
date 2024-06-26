#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2024, Francisco Fernandez
# License: CC BY-SA 4.0
#   https://github.com/fernandezfran/thesis/blob/main/LICENSE
import matplotlib.pyplot as plt
import pandas as pd

fig, ax = plt.subplots()

plt.rcParams.update({"font.size": 12})

aleaciones = ["Li12Si7", "Li7Si3", "Li13Si4", "Li15Si4"]
for k, aleacion in enumerate(aleaciones):
    dataset = pd.read_csv(f"datasets/c-{aleacion}.csv")

    ax.scatter(dataset.ppm, dataset.exp, s=5, color="k", zorder=2)
    ax.plot(dataset.ppm, dataset.pred, color="tab:blue", linewidth=3, zorder=1)

    ax.text(-30, 7.5 + 2.1 * (k + 0.2), aleacion)

ax.text(30, 16.4, "Si enlazados")
ax.vlines(18.0, 6, 17, color="k", linestyles="dashed")

ax.text(7.5, 16.4, "Si aislados")
ax.vlines(6.0, 6, 17, color="k", linestyles="dashed")

ax.set_xlim((50, -50))
ax.set_xlabel(r"$\delta$ (ppm)", fontsize=13)

ax.set_ylim((7.5, 16.2))
ax.set_yticks([])

fig.tight_layout()
fig.savefig("c-nmr.png", dpi=600)
