#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2024, Francisco Fernandez
# License: CC BY-SA 4.0
#   https://github.com/fernandezfran/thesis/blob/main/LICENSE
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

plt.rcParams.update({"font.size": 12})

experimental_dataset = pd.read_csv("datasets/fvc/afm.csv")

xdft = np.array([0, 4.25])
ydft = 0.786647 * xdft + 0.01547

numerical_dataset = pd.read_csv(
    "datasets/fvc/fvc.dat", delimiter=" ", names=["x", "fvc"]
)

fig, ax = plt.subplots()

ax.plot(
    experimental_dataset.x,
    experimental_dataset.afm,
    marker="s",
    linestyle="--",
    color="tab:blue",
    label="AFM",
)
ax.plot(xdft, ydft, color="k", label="DFT volumen fijo")
ax.plot(
    numerical_dataset.x,
    numerical_dataset.fvc,
    marker="o",
    linestyle="--",
    color="tab:orange",
    label="ReaxFF",
)

ax.set_xlim((0, 4.25))
ax.set_xlabel(r"$x$ en Li$_x$Si")
ax.secondary_xaxis(
    "top", functions=(lambda x: 4056.2 * x / 4.25, lambda x: 4056.2 * x / 4.25)
).set_xlabel(r"Capacidad (mAhg$^{-1}$)")

ax.set_ylim((-0.25, 3.5))
ax.set_ylabel("Cambio de volumen fraccionario")
ax.grid(axis="y", linestyle=":")

ax.legend()

fig.tight_layout()
fig.savefig("fvc.png", dpi=600)
