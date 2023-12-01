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


fig, ax = plt.subplots(nrows=1, ncols=3, figsize=(12, 4))

cmap = _colormap()

sm = plt.cm.ScalarMappable(cmap=cmap, norm=plt.Normalize(vmin=0, vmax=4.2))
clb = fig.colorbar(sm, ax=ax[0], ticks=[0, 1, 2, 3, 4], location="left")
clb.ax.set_ylabel(r"$x$ en Li$_x$Si")

xvals = ["0.21", "0.62", "1.25", "1.71", "2.17", "2.71", "3.25", "3.75", "4.20"]
for i, (central, interact) in enumerate(zip(["Li", "Si", "Si"], ["Li", "Li", "Si"])):
    weight = 5 if i == 2 else 1

    for j, x in enumerate(xvals):
        dataset = pd.read_csv(
            f"datasets/{central}{interact}/{x}.dat",
            delimiter="\s+",
            comment="#",
            names=["rdfx", "rdfy"],
        )
        ax[i].plot(dataset.rdfx, dataset.rdfy + j * weight, color=cmap(float(x)))

    ax[i].set_xlim((1.5, 10))
    ax[i].set_xlabel(r"r [$\AA$]")

    ax[i].set_ylabel("")
    ax[i].set_yticks([])

    ax[i].set_title(f"{central}-{interact}")
    ax[i].grid(linestyle=":")

ax[0].tick_params(labelleft=False)

ax[2].set_ylabel("RDF")
ax[2].yaxis.set_label_position("right")
ax[2].yaxis.set_ticks_position("right")
ax[2].yaxis.tick_right()

fig.tight_layout()
fig.savefig("rdf.png", dpi=600)
