#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2024, Francisco Fernandez
# License: CC BY-SA 4.0
#   https://github.com/fernandezfran/thesis/blob/main/LICENSE
import os

import itertools as it
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

plt.rcParams.update({"font.size": 16})
cmap = cm.get_cmap("viridis")

fig, ax = plt.subplots(figsize=(12, 5))

ax.set_xlabel("SOC")
ax.set_ylabel(r"$E - E^0$ (V)")
ax.set_xlim((0, 1.05))
ax.set_ylim((-0.4, 0.2))

ax.plot([0, 1.05], [-0.2, -0.2], ls="--", c="k")

ax.text(0.5, -0.35, "UMBEM")
ax.text(0.7, 0.1, "C-rate = 4 C")

for umbem in (0.3, 0.8, 1.0):
    data = np.loadtxt(f"_data/{umbem}.dat", dtype=np.float32, skiprows=1, unpack=True)
    x, potential = data[0], data[2]

    ax.plot(umbem * x / np.max(x), potential / 0.75, color=cmap(umbem))

    ax.scatter(umbem, -0.2, s=80, facecolors="none", edgecolors=cmap(umbem))

    dx = 0.025 if umbem < 0.5 else -0.025
    ax.arrow(
        0.58,
        -0.3,
        umbem - 0.58 + dx,
        0.09,
        color=cmap(umbem),
        head_width=0.01,
        head_length=0.01,
        overhang=1,
    )

# fig.tight_layout()
fig.savefig("_umbem.png", dpi=600)
plt.show()
