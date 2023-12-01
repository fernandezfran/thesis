#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2024, Francisco Fernandez
# License: CC BY-SA 4.0
#   https://github.com/fernandezfran/thesis/blob/main/LICENSE
import matplotlib.colors
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

plt.rcParams.update({"font.size": 16})


def _color_fader(mix, first_color="tab:blue", second_color="tab:green"):
    return matplotlib.colors.to_hex(
        (1 - mix) * np.array(matplotlib.colors.to_rgb(first_color))
        + mix * np.array(matplotlib.colors.to_rgb(second_color))
    )


fig, ax = plt.subplots(ncols=2, figsize=(13, 5))

xvals = [0.21, 0.62, 1.25, 1.71, 2.17, 2.71, 3.25, 3.75, 4.2]
n_silicios = [667, 670, 671, 672, 319, 319, 320, 288, 320]
markers = ["o", "v", "^", "<", ">", "s", "d", "D", "X"]
for i, (x, nsi, m) in enumerate(zip(xvals, n_silicios, markers)):
    dataset = pd.read_csv(
        f"datasets/{x}.dat",
        delimiter="\t",
        comment="#",
        names=["rcut", "nclusters", "lcluster", "isolatedp"],
    )

    color = _color_fader(x / 4.2)

    ax[0].plot(
        dataset.rcut,
        dataset.isolatedp,
        marker=m,
        color=color,
        linestyle="--",
        linewidth=1,
        label=x,
    )

    ax[1].plot(
        dataset.rcut,
        dataset.nclusters / nsi,
        marker=m,
        color=color,
        linestyle="--",
        linewidth=1,
        label=x,
    )

ax[0].set_xlabel(r"r$_{cut}$ [$\AA$]")
ax[0].set_ylabel(r"Fracción de átomos de Si aislados")
ax[0].grid(axis="both", linestyle=":")

ax[1].set_xlabel(r"r$_{cut}$ [$\AA$]")
ax[1].set_ylabel(r"Cantidad de clusters de Si / N$_{Si}$")
ax[1].grid(axis="both", linestyle=":")

handles, labels = ax[1].get_legend_handles_labels()
ax[1].legend(handles[::-1], labels[::-1], title=r"$x$ en Li$_x$Si", loc=1, fontsize=14)

ax[0].text(0.0, 1.05, "(a)", transform=ax[0].transAxes)
ax[1].text(0.92, 1.05, "(b)", transform=ax[1].transAxes)

fig.tight_layout()
fig.savefig("clusters.png", dpi=600)
