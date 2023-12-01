#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2024, Francisco Fernandez
# License: CC BY-SA 4.0
#   https://github.com/fernandezfran/thesis/blob/main/LICENSE
import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams.update({"font.size": 12})

fig, ax = plt.subplots()

dataset = pd.read_csv("dataset.csv")

for interaccion, m, c in zip(
    ["LiLi", "SiLi", "SiSi"], ["o", "^", "s"], ["tab:green", "tab:orange", "tab:blue"]
):
    ax.plot(
        dataset["x"],
        dataset[interaccion],
        marker=m,
        color=c,
        linestyle="dashed",
        label=interaccion,
    )

ax.set_xlim((0, 4.25))
ax.set_xlabel(r"$x$ en Li$_x$Si")
ax.secondary_xaxis(
    "top", functions=(lambda x: 4056.2 * x / 4.25, lambda x: 4056.2 * x / 4.25)
).set_xlabel(r"Capacidad (mAhg$^{-1}$)")

ax.set_ylabel(r"$\theta$")
ax.grid(axis="y", linestyle=":")

ax.legend()

fig.tight_layout()
fig.savefig("sro.png", dpi=600)
