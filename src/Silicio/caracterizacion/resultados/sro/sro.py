#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2024, Francisco Fernandez
# License: CC BY-SA 4.0
#   https://github.com/fernandezfran/thesis/blob/main/LICENSE

"""Short range order vs x."""

import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({"font.size": 12})
fig, ax = plt.subplots()

ax.set_xlabel(r"$x$ en Li$_x$Si")
ax.secondary_xaxis(
    "top", functions=(lambda x: 4056.2 * x / 4.25, lambda x: 4056.2 * x / 4.25)
).set_xlabel(r"Capacidad (mAhg$^{-1}$)")
ax.set_ylabel(r"$\theta$")

ax.grid(axis="y", linestyle=":")

ax.set_xlim((0, 4.25))

x, sili, lili, sisi = np.loadtxt("theta.dat", unpack=True)
plt.plot(x, lili, marker="o", color="tab:green", linestyle="dashed", label="LiLi")
plt.plot(x, sili, marker="^", color="tab:orange", linestyle="dashed", label="SiLi")
plt.plot(x, sisi, marker="s", color="tab:blue", linestyle="dashed", label="SiSi")

ax.legend()
fig.tight_layout()

fig.savefig("sro.png", dpi=600)
