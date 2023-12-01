#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2024, Francisco Fernandez
# License: CC BY-SA 4.0
#   https://github.com/fernandezfran/thesis/blob/main/LICENSE
from shared import *

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 5))

ax1.text(-3.9, 1, "Zona de carga rápida")
ax1.text(-1.5, -3, "Zona de carga lenta", color="white")

greg = galpynostatic.model.GalvanostaticRegressor(spherical, 1, 1)
greg._map = galpynostatic.datasets.map.MapSpline(spherical)
ax1 = greg.plot.render_map(ax=ax1, clb_label="UMBEM")

X, Y = np.linspace(-6, 6), np.linspace(-6, 6)
Z = greg._map.soc(X, Y, grid=True).T
ax1.contour(
    X,
    Y,
    Z,
    levels=np.array([0.8]),
    colors="tab:gray",
    linewidths=2,
    linestyles="dashed",
)

ax1.text(-2.85, -3.05, r"$k^0$")
ax1.arrow(
    -3,
    -3.45,
    0,
    0.7,
    color="k",
    length_includes_head=True,
    head_width=0.1,
    head_length=0.125,
)
ax1.scatter(-3, -3.45, marker="s", color="tab:red")

ax1.text(0, 1.1, r"$d$")
ax1.arrow(
    0.5,
    1,
    -0.7,
    0,
    color="k",
    length_includes_head=True,
    head_width=0.1,
    head_length=0.125,
)

ax1.text(0.25, 0.5, r"$D$")
ax1.arrow(
    0.5,
    1,
    -0.7,
    -0.7,
    color="k",
    length_includes_head=True,
    head_width=0.1,
    head_length=0.125,
)
ax1.scatter(0.5, 1, marker="o", color="tab:red")

ax1.set_xlim((-4, 2))
ax1.set_ylim((-4, 2))

ax1.set_xticks([])
ax1.set_yticks([])

w = 0.02
x = np.linspace(0, 1, num=len(socs.keys()))
for i, (ops, soc) in enumerate(zip(opss.values(), socs.values())):
    colors = [cmap(v) for v in soc]
    xs = np.linspace(
        x[i] - (w / 2) * len(ops), x[i] + (w / 2) * len(ops), num=len(ops)
    )
    ax2.bar(xs, ops, width=w, color=colors)

ax2.axhline(y=1, color="tab:gray", linestyle="dashed", linewidth=1)

ax2.set_xticks(x)
ax2.set_xticklabels(opss.keys())

ax2.set_yscale("log")
ax2.set_ylim((0.01, 30))
ax2.set_ylabel(r"$\log{\left(d_{opt} / d_{exp}\right)}$")

fig.tight_layout()
fig.savefig("sizes.png", dpi=600)
