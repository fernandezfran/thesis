#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Fractional volume change versus x."""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

nordred = "#BF616A"
nordblue = "#5E81AC"
nordgray = "#2E3440"

x, fvc = np.loadtxt("_data/fvc/fvc.dat", unpack=True)
df = pd.read_csv("_data/fvc/afm.csv")
xdft = np.array([0, 4.25])

plt.rcParams.update({"font.size": 12})
fig, ax = plt.subplots()

ax.set_xlabel(r"$x$ en Li$_x$Si")
ax.secondary_xaxis(
    "top", functions=(lambda x: 4056.2 * x / 4.25, lambda x: 4056.2 * x / 4.25)
).set_xlabel(r"Capacidad [mAhg$^{-1}$]")
ax.set_ylabel("Cambio de volumen fraccionario")

ax.grid(axis="y", linestyle=":")

ax.set_ylim((-0.25, 3.5))
ax.set_xlim((0, 4.25))

ax.plot(x, fvc, marker="o", linestyle="--", color=nordred, label="ReaxFF")
ax.plot(df.x, df.afm, marker="s", linestyle="--", color=nordblue, label="AFM")
ax.plot(xdft, 0.786647 * xdft + 0.001547, color=nordgray, label="DFT volumen fijo")

ax.legend()
fig.tight_layout()

fig.savefig("fvc.png", dpi=600)
