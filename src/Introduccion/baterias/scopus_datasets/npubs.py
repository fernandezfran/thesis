#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2024, Francisco Fernandez
# License: CC BY-SA 4.0
#   https://github.com/fernandezfran/thesis/blob/main/LICENSE
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

files = [
    "lithium_battery.csv",
    "lithium_battery_fast-charging.csv",
    "lithium_battery_Si-anodes.csv",
]
markers = ["s", "^", "o"]
labels = ["LIBs", "Carga rápida", "Ánodos de Si"]

fig, ax = plt.subplots()

for file, marker, label in zip(files, markers, labels):
    dataset = pd.read_csv(file)

    ax.plot(
        dataset["year"],
        dataset["npub"] / dataset["npub"].iloc[-1],
        marker=marker,
        ls="--",
        label=label,
    )

ax.legend()

ax.set_xlim((2003, 2023))
ax.set_xticks(np.arange(2003, 2024, 2))
ax.set_xlabel("Año")

ax.set_ylabel("Número de publcaciones anuales normalizado")
ax.set_yscale("log")

fig.tight_layout()
fig.savefig("../scopus.png", dpi=600)
