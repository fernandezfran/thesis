#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2024, Francisco Fernandez
# License: CC BY-SA 4.0
#   https://github.com/fernandezfran/thesis/blob/main/LICENSE
from macchiato.utils import voigt_peak
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


fig, ax = plt.subplots()

plt.rcParams.update({"font.size": 12})

x = np.linspace(-20, 60, num=500)

ax.text(-1, 0.1, "referencia")

ax.text(20, 0.35, "menor")
ax.text(23, 0.325, "apantallamiento")
ax.plot(x, voigt_peak(x, 20, 0.05, 1.0))

ax.text(45, 0.35, "mayor")
ax.text(48, 0.325, "apantallamiento")
ax.plot(x, voigt_peak(x, 40, 0.05, 1.0))

ax.vlines(0.0, 0.0, 1.0, color="k", linestyles="dashed")

ax.set_xlim((60, -20))
ax.set_xticks([50, 0, -10], [r"$+ \delta$", "0", r"$- \delta$"])
ax.set_xlabel(r"$\delta$ (ppm)", fontsize=13)

ax.set_ylim((0, 0.4))
ax.set_yticks([])

fig.tight_layout()
fig.savefig("_corrimiento_quimico.png", dpi=600)
