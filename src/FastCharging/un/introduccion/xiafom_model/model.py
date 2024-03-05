#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2024, Francisco Fernandez
# License: CC BY-SA 4.0
#   https://github.com/fernandezfran/thesis/blob/main/LICENSE
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np
from scipy.special import erf

plt.rcParams.update({"font.size": 12})

xvals = np.linspace(0, 2, num=500)

fig, ax = plt.subplots(figsize=(8, 5))

ax.add_patch(Rectangle((0, 0), 1, 1, alpha=0.5, color="tab:blue"))

ax.plot(xvals, erf(0.5 * xvals), color="tab:orange")
ax.plot(xvals, erf(xvals), ls="--", color="tab:orange")
ax.plot(xvals, erf(2 * xvals), ls="--", color="tab:orange")
ax.plot(xvals, erf(5 * xvals), ls="--", color="tab:orange")
ax.plot(xvals, erf(10 * xvals), color="tab:orange")

ax.set_xticks([0, 1, 2], ["0", "L", "2L"])
ax.set_yticks([0, 0.5, 1], [0, r"0.5$c_b$", r"$c_b$"])

ax.set_xlim((0, 2))
ax.set_ylim((0, 1.05))

ax.text(1.1, 0.25, r"$c(x, t) = c_b erf\left(\frac{x}{2\sqrt{D t}}\right)$")
ax.text(0.7, 0.15, r"$\tau = \frac{L^2}{D}$")

ax.text(0.05, 1.01, r"$10^{-4}\tau$")
ax.text(0.3, 0.9, r"$10^{-3}\tau$")
ax.text(0.5, 0.8, r"$10^{-2}\tau$")
ax.text(0.7, 0.6, r"$10^{-1}\tau$")
ax.text(0.75, 0.45, r"$\tau$")

ax.text(-0.4, 0.9, "Se supone")
ax.text(-0.4, 0.85, "una cinética")
ax.text(-0.4, 0.8, "interfacial")
ax.text(-0.4, 0.75, "ultrarápida")

fig.tight_layout()
fig.savefig("model.png")
