#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2024, Francisco Fernandez
# License: CC BY-SA 4.0
#   https://github.com/fernandezfran/thesis/blob/main/LICENSE
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

plt.rcParams.update({"font.size": 12})

fig, ax = plt.subplots()

for file, label in zip(
    ["ev-value.csv", "combustion-value.csv"], ["eléctrico", "a combustión interna"]
):
    dataset = pd.read_csv(file)

    cheby = np.polynomial.chebyshev.Chebyshev.fit(dataset.year, dataset.cost, deg=4)

    ax.plot(dataset.year, cheby(dataset.year), lw=2, label=label)

ax.set_xticks(range(2016, 2031, 2))
ax.set_xlabel("Año")

ax.set_ylim((0, 45000))
ax.set_ylabel("Costo de vehículos medianos (USD$)")

ax.legend(title="Vehículo")

fig.tight_layout()
fig.savefig("ev-value.png", dpi=600)
