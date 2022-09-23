#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Todos los histogramas de energias potencial."""

import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter
import numpy as np

nordred = "#BF616A"
nordblue = "#5E81AC"
nordgreen = "#A3BE8C"
nordorange = "#D08770"
nordgray = "#2E3440"

nordcolors = [nordgray, nordgreen, nordblue, nordorange, nordred]
alfas = [1, 0.2, 0.4, 0.6, 0.8]
concentraciones = np.array([[0.21, 0.62, 1.25], [1.71, 2.17, 2.71], [3.25, 3.75, 4.2]])
anchos = np.array(
    [[0.002, 0.001, 0.0009], [0.0009, 0.0009, 0.0009], [0.0009, 0.0009, 0.0009]]
)

plt.rcParams.update({"font.size": 10})
fig, axes = plt.subplots(3, 3, sharey="row")

fig.text(0.5, 0.005, "E / N [eV]", ha="center")
fig.text(0.005, 0.5, "frecuencias", va="center", rotation="vertical")

for conc, axis, anch in zip(concentraciones, axes, anchos):
    for x, ax, w in zip(conc, axis, anch):

        ax.grid(axis="x", linestyle=":")
        ax.set_ylim((0.0, 0.3))

        ax.xaxis.set_major_formatter(FormatStrFormatter("%.2f"))

        if x in [0.21, 2.17, 4.2]:
            xx, yy = np.loadtxt(f"_data/energias/md/{x}.dat", unpack=True)
            ax.bar(
                xx,
                yy,
                width=w,
                color=nordgray,
                alpha=0.75,
                label=rf"$\alpha$ = 1",
            )

        histo = np.loadtxt(f"_data/energias/{x}-histo.dat", unpack=True)
        for c, h, alfa in zip(nordcolors[1:], histo[1:], alfas[1:]):
            ax.bar(
                histo[0],
                h,
                width=w,
                color=c,
                alpha=0.75,
                label=rf"$\alpha$ = {alfa}",
            )

        ax.text(0.1, 1.02, f"x = {x}", transform=ax.transAxes)

        if x == 1.25:
            ax.legend(bbox_to_anchor=(1.04, 1), loc="upper left", prop={"size": 8})

fig.subplots_adjust(wspace=0.05, hspace=0.25)
fig.tight_layout()

fig.savefig("energias.png", dpi=600)
