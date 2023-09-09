#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Radial Distribution Function.

Correr como:

    $ python3 rdf.py ij

donde ij es el tipo de interacción posible: LiLi, SiSi o SiLi.
"""

import sys

import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np


def color_fader(mix):
    nordblue = np.array(colors.to_rgb("#5E81AC"))
    nordgreen = np.array(colors.to_rgb("#A3BE8C"))
    return colors.to_hex((1 - mix) * nordblue + mix * nordgreen)


path = f"data/{sys.argv[1]}/"
concentraciones = [0.21, 0.62, 1.25, 1.71, 2.17, 2.71, 3.25, 3.75, 4.2]
n = len(concentraciones)

weight = 1
if sys.argv[1] == "SiSi":
    weight = 5

e1 = sys.argv[1][:2]
e2 = sys.argv[1][2:]

plt.rcParams.update({"font.size": 16})
fig, ax = plt.subplots()

ax.set_xlabel(r"r [$\AA$]")
ax.set_ylabel(rf"RDF {e1}-{e2}")

ax.grid(axis="x", linestyle=":")

ax.set_xlim((1.5, 10))
ax.set_yticks([])

for i, x in enumerate(concentraciones):
    rdfx, rdfy = np.loadtxt(path + f"{x}.dat", unpack=True)
    ax.plot(rdfx, rdfy + i * weight, color=color_fader(i / n), label=f"{x}")

if sys.argv[1] == "LiLi":
    handles, labels = ax.get_legend_handles_labels()
    ax.legend(handles[::-1], labels[::-1], title=r"$x$ en Li$_x$Si", loc=1)

fig.tight_layout()
fig.savefig(f"rdf-{sys.argv[1]}.png", dpi=600)
