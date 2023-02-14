#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Porcentaje de átomos de Si aislados en función del radio de corte."""

import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np


def color_fader(mix):
    nordblue = np.array(colors.to_rgb("#5E81AC"))
    nordgreen = np.array(colors.to_rgb("#A3BE8C"))
    return colors.to_hex((1 - mix) * nordblue + mix * nordgreen)


concentraciones = [0.21, 0.62, 1.25, 1.71, 2.17, 2.71, 3.25, 3.75, 4.2]
nsis = [667, 670, 671, 672, 319, 319, 320, 288, 320]
n = len(concentraciones)

plt.rcParams.update({"font.size": 16})
fig, ax = plt.subplots()

ax.set_xlabel(r"r$_{cut}$ [$\AA$]")
ax.set_ylabel(r"Cantidad de clusters de Si / N$_{Si}$")

ax.grid(axis="both", linestyle=":")

markers = ["o", "v", "^", "<", ">", "s", "d", "D", "X"]
for i, (x, m, natoms) in enumerate(zip(concentraciones, markers, nsis)):
    rcut, nclusters, lcluster, isolatedp = np.loadtxt(
        f"data/{x}.dat", unpack=True
    )
    ax.plot(
        rcut,
        nclusters / natoms,
        marker=m,
        color=color_fader(i / n),
        linestyle="dashed",
        linewidth=1,
        label=f"{x}",
    )

handles, labels = ax.get_legend_handles_labels()
ax.legend(handles[::-1], labels[::-1], title=r"$x$ en Li$_x$Si", loc=1)

fig.tight_layout()
fig.savefig(f"cluster-nclusters.png", dpi=600)
