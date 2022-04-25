#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""CN vs x."""

import matplotlib.pyplot as plt
import numpy as np

nordblue = "#5E81AC"
nordgreen = "#A3BE8C"
nordorange = "#D08770"

fig, ax = plt.subplots()

ax.set_xlabel(r"$x$ en Li$_x$Si")
ax.secondary_xaxis(
    "top", functions=(lambda x: 4056.2 * x / 4.25, lambda x: 4056.2 * x / 4.25)
).set_xlabel(r"Capacidad [mAhg$^{-1}$]")
ax.set_ylabel("CN")

ax.grid(axis="y", linestyle=":")

ax.set_xlim((0, 4.25))

interacciones = ["LiLi", "SiLi", "SiSi"]
colores = [nordgreen, nordorange, nordblue]
markers = ["o", "^", "s"]
for e, c, m in zip(interacciones, colores, markers):
    x, y, yerr = np.loadtxt(f"_data/cn2/{e}.dat", unpack=True)
    ax.errorbar(
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

ax.legend()
fig.tight_layout()

fig.savefig("cn2.png", dpi=600)
