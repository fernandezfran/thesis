#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2024, Francisco Fernandez
# License: CC BY-SA 4.0
#   https://github.com/fernandezfran/thesis/blob/main/LICENSE
import matplotlib.colors
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

plt.rcParams.update({"font.size": 16})


def _color_fader(mix, first_color="tab:blue", second_color="tab:green"):
    return matplotlib.colors.to_hex(
        (1 - mix) * np.array(matplotlib.colors.to_rgb(first_color))
        + mix * np.array(matplotlib.colors.to_rgb(second_color))
    )


def _colormap():
    return matplotlib.colors.ListedColormap(
        [_color_fader(v) for v in np.linspace(0, 1, num=100)]
    )


fig, ax = plt.subplots(nrows=1, ncols=3, sharey=True, figsize=(12, 4))

cmap = _colormap()

sm = plt.cm.ScalarMappable(cmap=cmap, norm=plt.Normalize(vmin=0, vmax=3.75))
clb = fig.colorbar(sm, ax=ax[0], ticks=[0, 1, 2, 3, 3.75], location="left")
clb.ax.set_ylabel(r"$x$ en Li$_x$Si")

for k, (central, interact) in enumerate(zip(["Li", "Si", "Si"], ["Li", "Li", "Si"])):

    xvals = ["0.20", "0.56", "0.89", "1.50", "2.00", "2.50", "3.28", "3.75"]

    for x in xvals:
        dataset = pd.read_csv(f"datasets/rdf-{x}-{central}-{interact}.csv")
        ax[k].plot(dataset.r, dataset.rdf, color=cmap(float(x) / 3.75))

    ax[k].set_xlim((1.5, 6))
    ax[k].set_xlabel(r"r [$\AA$]")

    ax[k].set_ylabel("")

    ax[k].set_title(f"{central}-{interact}")

    ax[k].grid(linestyle=":")

    if k == 2:
        ax[k].yaxis.set_label_position("right")
        ax[k].yaxis.set_ticks_position("right")
        ax[k].yaxis.tick_right()
        ax[k].set_ylabel("RDF")
    elif k == 0:
        ax[k].tick_params(labelleft=False)

fig.tight_layout()
fig.savefig("prdfs.png", dpi=600)
