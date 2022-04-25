#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Histograma de áreas de interconexiones."""

import matplotlib.pyplot as plt
import numpy as np

nordgreen = "#A3BE8C"
nordpink = "#B48EAD"

fig, ax = plt.subplots()

ax.set_xlabel(r"$x$ en Li$_x$Si")
ax.secondary_xaxis(
    "top", functions=(lambda x: 4056.2 * x / 4.25, lambda x: 4056.2 * x / 4.25)
).set_xlabel(r"Capacidad [mAhg$^{-1}$]")
ax.set_ylabel("Fracción")

ax.grid(axis="y", linestyle=":")

ax.set_xlim((0, 4.35))


x, h1, h2 = np.loadtxt("_data/interconexion/areas/histo.dat", unpack=True)

w = 0.1
ax.bar(x - 0.5 * w, h1, width=w, color=nordpink, label="una conexión")
ax.bar(x + 0.5 * w, h2, width=w, color=nordgreen, label="más de una conexión")

ax.legend()

fig.tight_layout()

fig.savefig("interconexiones-areas.png", dpi=600)
