#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Porcentaje de átomos de Si aislados en función del radio de corte."""

import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np


def color_fader(mix):
    nordblue = np.array(colors.to_rgb("tab:blue"))
    nordgreen = np.array(colors.to_rgb("tab:green"))
    return colors.to_hex((1 - mix) * nordblue + mix * nordgreen)


plt.rcParams.update({"font.size": 16})

concentraciones = [0.21, 0.62, 1.25, 1.71, 2.17, 2.71, 3.25, 3.75, 4.2]
nsis = [667, 670, 671, 672, 319, 319, 320, 288, 320]

fig, ax = plt.subplots(ncols=2, figsize=(13, 5))

ax[0].set_xlabel(r"r$_{cut}$ [$\AA$]")
ax[0].set_ylabel(r"Fracción de átomos de Si aislados")

ax[0].grid(axis="both", linestyle=":")

ax[1].set_xlabel(r"r$_{cut}$ [$\AA$]")
ax[1].set_ylabel(r"Cantidad de clusters de Si / N$_{Si}$")

ax[1].grid(axis="both", linestyle=":")

markers = ["o", "v", "^", "<", ">", "s", "d", "D", "X"]
for i, (x, m, natoms) in enumerate(zip(concentraciones, markers, nsis)):
    rcut, nclusters, lcluster, isolatedp = np.loadtxt(f"data/{x}.dat", unpack=True)

    color = color_fader(x / 4.2)

    ax[0].plot(
        rcut,
        isolatedp,
        marker=m,
        color=color,
        linestyle="--",
        linewidth=1,
        label=x,
    )

    ax[1].plot(
        rcut,
        nclusters / natoms,
        marker=m,
        color=color,
        linestyle="--",
        linewidth=1,
        label=x,
    )

handles, labels = ax[1].get_legend_handles_labels()
ax[1].legend(handles[::-1], labels[::-1], title=r"$x$ en Li$_x$Si", loc=1, fontsize=14)

ax[0].text(0.0, 1.05, "(a)", transform=ax[0].transAxes)
ax[1].text(0.92, 1.05, "(b)", transform=ax[1].transAxes)

fig.tight_layout()
fig.savefig("clusters.png", dpi=600)
