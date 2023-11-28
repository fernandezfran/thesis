#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2024, Francisco Fernandez
# License: CC BY-SA 4.0
#   https://github.com/fernandezfran/thesis/blob/main/LICENSE

"""CN vs x."""

import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({"font.size": 16})

fig, ax = plt.subplots(ncols=2, figsize=(13, 5))

ax[0].set_ylabel("CN")
for axis in ax:
    axis.set_xlabel(r"$x$ en Li$_x$Si")
    axis.secondary_xaxis(
        "top", functions=(lambda x: 4056.2 * x / 4.25, lambda x: 4056.2 * x / 4.25)
    ).set_xlabel(r"Capacidad (mAhg$^{-1}$)")
    axis.grid(axis="y", linestyle=":")
    axis.set_xlim((0, 4.25))

interacciones = ["LiLi", "SiLi", "SiSi"]
colores = ["tab:green", "tab:orange", "tab:blue"]
markers = ["o", "^", "s"]
for e, c, m in zip(interacciones, colores, markers):
    x, y, yerr = np.loadtxt(f"data/cn/{e}.dat", unpack=True)
    ax[0].errorbar(
        x,
        y,
        yerr=yerr,
        marker=m,
        color=c,
        linestyle="dashed",
        linewidth=1,
        capsize=2.5,
        elinewidth=1,
        label=f"{e}",
    )

    x, y, yerr = np.loadtxt(f"data/cn2/{e}.dat", unpack=True)
    ax[1].errorbar(
        x,
        y,
        yerr=yerr,
        marker=m,
        color=c,
        linestyle="dashed",
        linewidth=1,
        capsize=2.5,
        elinewidth=1,
        label=f"{e}",
    )

ax[0].legend()

ax[0].text(0.0, 1.15, "(a)", transform=ax[0].transAxes)
ax[1].text(0.92, 1.15, "(b)", transform=ax[1].transAxes)

fig.tight_layout()
fig.savefig("cn.png", dpi=600)
