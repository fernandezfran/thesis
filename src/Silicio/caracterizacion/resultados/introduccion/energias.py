#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2024, Francisco Fernandez
# License: CC BY-SA 4.0
#   https://github.com/fernandezfran/thesis/blob/main/LICENSE

"""Todos los histogramas de energias potencial."""

import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter
import numpy as np

colors = ["tab:gray", "tab:green", "tab:blue", "tab:orange", "tab:red"]
alfas = [1, 0.2, 0.4, 0.6, 0.8]
concentraciones = np.array([[0.21, 0.62, 1.25], [1.71, 2.17, 2.71], [3.25, 3.75, 4.2]])
anchos = np.array(
    [[0.002, 0.001, 0.0009], [0.0009, 0.0009, 0.0009], [0.0009, 0.0009, 0.0009]]
)

plt.rcParams.update({"font.size": 10})
fig, axes = plt.subplots(3, 3, sharey="row")

fig.text(0.5, 0.005, "E / N (eV)", ha="center")
fig.text(0.005, 0.5, "frecuencias", va="center", rotation="vertical")

for conc, axis, anch in zip(concentraciones, axes, anchos):
    for x, ax, w in zip(conc, axis, anch):

        ax.grid(axis="x", linestyle=":")
        ax.set_ylim((0.0, 0.3))

        ax.xaxis.set_major_formatter(FormatStrFormatter("%.2f"))

        histo = np.loadtxt(f"data/{x}-histo.dat", unpack=True)
        for c, h, alfa in zip(colors[1:], histo[1:], alfas[1:]):
            ax.bar(
                histo[0],
                h,
                width=w,
                color=c,
                alpha=0.75,
                label=rf"$\alpha$ = {alfa}",
            )

        if x in [0.21, 2.17, 4.2]:
            xx, yy = np.loadtxt(f"data/md/{x}.dat", unpack=True)
            ax.bar(
                xx,
                yy,
                width=w,
                color="tab:gray",
                alpha=0.75,
                label=rf"$\alpha$ = 1",
            )

        ax.text(0.1, 1.02, f"x = {x}", transform=ax.transAxes)

        if x == 4.2:
            ax.legend(bbox_to_anchor=(1.04, 1), loc="upper left", prop={"size": 8})

fig.subplots_adjust(wspace=0.05, hspace=0.25)
fig.tight_layout()

fig.savefig("energias.png", dpi=600)
