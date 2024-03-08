#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2024, Francisco Fernandez
# License: CC BY-SA 4.0
#   https://github.com/fernandezfran/thesis/blob/main/LICENSE
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def absorption_peak(x, x0, gamma):
    return -gamma / (gamma ** 2 + (x - x0) ** 2) / np.pi


plt.rcParams.update({"font.size": 14})

fig, ax = plt.subplots(figsize=(6.0, 5.5))

xvals = np.linspace(-2, 2, num=500)

ax.plot(
    xvals,
    0.75 * (absorption_peak(xvals, 0.3 - 0.01, 0.1) + absorption_peak(xvals, 0.3 + 0.01, 0.1)),
)
ax.text(-1.4, 0.1, r"$\delta$: desplazamiento isomérico")

ax.plot(xvals, absorption_peak(xvals, 0.3 - 0.2, 0.1) + absorption_peak(xvals, 0.3 + 0.2, 0.1) - 5)
ax.text(-1.4, -4.95, r"$\Delta$: división cuadrupolar")

ax.set_xlim((-1.5, 1.5))
ax.set_xticks([-1, 0, 1], ["-v", 0, "+v"])
ax.set_xlabel("Velocidad (mm/s)")

ax.set_ylim((-9, 1))
ax.set_yticks([])
ax.set_ylabel("Espectro de absorción")

fig.tight_layout()
fig.savefig("_mossbauer_diagram.png", dpi=600)
