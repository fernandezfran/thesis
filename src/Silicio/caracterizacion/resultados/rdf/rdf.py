#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2024, Francisco Fernandez
# License: CC BY-SA 4.0
#   https://github.com/fernandezfran/thesis/blob/main/LICENSE
import matplotlib.colors
import matplotlib.pyplot as plt

import numpy as np

import pandas as pd

def _color_fader(mix, first_color="tab:blue", second_color="tab:green"):
    """Color fader function."""
    c1 = np.array(matplotlib.colors.to_rgb(first_color))
    c2 = np.array(matplotlib.colors.to_rgb(second_color))
    return matplotlib.colors.to_hex((1 - mix) * c1 + mix * c2)


def _colormap():
    """Color map function generated with color fader function."""
    colors = [_color_fader(v) for v in np.linspace(0, 1, num=100)]
    return matplotlib.colors.ListedColormap(colors)

plt.rcParams.update({"font.size": 16})

fig, ax = plt.subplots(nrows=1, ncols=3, figsize=(12, 4))

cmap = _colormap()

sm = plt.cm.ScalarMappable(cmap=cmap, norm=plt.Normalize(vmin=0, vmax=4.2))
clb = fig.colorbar(sm, ax=ax[0], ticks=[0, 1, 2, 3, 4.0], location="left")
clb.ax.set_ylabel(r"$x$ en Li$_x$Si")

xs = ["0.21", "0.62", "1.25", "1.71", "2.17", "2.71", "3.25", "3.75", "4.20"]
for k, (weight, central, interact) in enumerate(zip([1, 1, 5], ["Li", "Si", "Si"], ["Li", "Li", "Si"])):

    for i, x in enumerate(xs):
        rdfx, rdfy = np.loadtxt(f"data/{central}{interact}/{x}.dat", unpack=True)
        ax[k].plot(rdfx, rdfy + i * weight, color=cmap(float(x) / 4.2))

    ax[k].set_xlabel(r"r [$\AA$]")
    ax[k].set_ylabel("")
    ax[k].set_title(f"{central}-{interact}")

    ax[k].set_xlim((1.5, 10))
    ax[k].set_yticks([])

    ax[k].grid(linestyle=":")

    if k == 2:
        ax[k].yaxis.set_label_position("right")
        ax[k].yaxis.set_ticks_position("right")
        ax[k].yaxis.tick_right()
        ax[k].set_ylabel("RDF")
    elif k == 0:
        ax[k].tick_params(labelleft=False)

fig.tight_layout()
fig.savefig("rdf.png", dpi=600)
