#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2024, Francisco Fernandez
# License: CC BY-SA 4.0
#   https://github.com/fernandezfran/thesis/blob/main/LICENSE
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

plt.rcParams.update({"font.size": 12})

fig, ax = plt.subplots(figsize=(1.1 * 7, 1.1 * 5))

ax.secondary_xaxis(
    "top", functions=(lambda x: 4056.2 * x / 4.25, lambda x: 4056.2 * x / 4.25)
).set_xlabel(r"Capacidad (mAhg$^{-1}$)")

for experimento, l in zip(["e", "f"], ["datos experimentales", None]):
    df = pd.read_csv(f"datos/lithiation-{experimento}.csv")
    ax.scatter(df.x, df.delta, color="k", marker="^", s=10, label=l)

xglobal = np.linspace(0, 4, num=500)
yglobal = 0.15 + 2.4 * (0.5 - np.abs((xglobal / (1 + xglobal)) - 0.5))
ax.plot(xglobal, yglobal, color="tab:orange", ls="--", label="concentraciones globales")
ax.text(0.35, 1.0, r"C$_{Li}$", rotation=60, color="tab:orange", fontsize="large")
ax.text(1.85, 1.0, r"C$_{Si}$", rotation=-30, color="tab:orange", fontsize="large")

df = pd.read_csv("datos/mossbauer.csv")
ax.scatter(df.x, df.delta, s=50, color="tab:blue", label="concentraciones locales")

ax.set_xlim((0, 4))
ax.set_ylim((0.15, 1.35))

ax.set_yticks(np.arange(0.2, 1.21, 0.2))

ax.secondary_yaxis(
    "right", functions=(lambda x: (x - 0.15)/2.4, lambda x: 2.4 * x + 0.15)
).set_ylabel(r"min{C$_{Li}$, C$_{Si}$}")

ax.set_xlabel(r"$x$ en Li$_x$Si")
ax.set_ylabel(r"$\Delta$ en los picos de Mössbauer (mm/s)")

ax.legend()

fig.tight_layout()
fig.savefig("mossbauer.png", dpi=600)
