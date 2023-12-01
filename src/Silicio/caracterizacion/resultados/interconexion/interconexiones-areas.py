#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2024, Francisco Fernandez
# License: CC BY-SA 4.0
#   https://github.com/fernandezfran/thesis/blob/main/LICENSE
import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams.update({"font.size": 12})

fig, ax = plt.subplots()

dataset = pd.read_csv("datasets/areas.csv")

ax.bar(dataset.x - 0.05, dataset.h1, width=0.1, label="una conexión")
ax.bar(dataset.x + 0.05, dataset.h2, width=0.1, label="más de una conexión")

ax.set_xlim((0, 4.35))
ax.set_xlabel(r"$x$ en Li$_x$Si")
ax.secondary_xaxis(
    "top", functions=(lambda x: 4056.2 * x / 4.25, lambda x: 4056.2 * x / 4.25)
).set_xlabel(r"Capacidad (mAhg$^{-1}$)")

ax.set_ylabel("Fracción")
ax.grid(axis="y", linestyle=":")

ax.legend()

fig.tight_layout()
fig.savefig("interconexiones-areas.png", dpi=600)
