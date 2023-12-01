#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2024, Francisco Fernandez
# License: CC BY-SA 4.0
#   https://github.com/fernandezfran/thesis/blob/main/LICENSE
from shared import *

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 5))

greg = galpynostatic.model.GalvanostaticRegressor(spherical, 1, 1)
greg._map = galpynostatic.datasets.map.MapSpline(spherical)
ax1 = greg.plot.render_map(ax=ax1, clb_label="UMBEM")

X, Y = np.linspace(-5, 6), np.linspace(-5, 6)
Z = greg._map.soc(X, Y, grid=True).T
ax1.contour(
    X,
    Y,
    Z,
    levels=np.array([0.8]),
    colors="tab:gray",
    linewidths=1,
    linestyles="dashed",
)

X = np.array([[4.0]])
for sys, dcoeff, d in zip(
    dataset["Material"], dataset["dcoeff_midpoint_cm2s"], dataset["d_mean_micro"]
):
    greg = galpynostatic.model.GalvanostaticRegressor(spherical, 1e-4 * d, 3)
    greg.dcoeff_, greg.k0_ = dcoeff, k0

    logell = galpynostatic.utils.logell(X, 1e-4 * d, 3, dcoeff)
    logxi = galpynostatic.utils.logxi(X, dcoeff, k0)

    ax1.scatter(logell, logxi, marker=marker[sys], color=color[sys], edgecolor="k")

for sys in systems:
    ax1.scatter(
        -100, -100, color=color[sys], marker=marker[sys], label=sys, edgecolor="k"
    )
ax1.legend(ncol=6, frameon=False, loc=(0.35, 1.05))

ax1.text(0, 1.05, "(a)", transform=ax1.transAxes)
ax2.text(0.95, 1.05, "(b)", transform=ax2.transAxes)

ax1.set_xlim((-4.25, 4.25))
ax1.set_ylim((-4, 4))

ax2.axhline(y=0.8, color="tab:gray", linestyle="dashed", linewidth=1)

x = np.linspace(0, 1, num=len(socs.keys()))
w = 0.02
for i, v in enumerate(socs.values()):
    colors = [cmap(soc) for soc in v]
    xs = np.linspace(x[i] - (w / 2) * len(v), x[i] + (w / 2) * len(v), num=len(v))
    ax2.bar(xs, v, width=w, color=colors)

ax2.set_xticks(x)
ax2.set_xticklabels(socs.keys())
ax2.set_ylim((0, 1))
ax2.set_ylabel("UMBEM")

plt.savefig("UMBEM.png", dpi=600)
