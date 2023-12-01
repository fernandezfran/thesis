#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2024, Francisco Fernandez
# License: CC BY-SA 4.0
#   https://github.com/fernandezfran/thesis/blob/main/LICENSE
import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams.update({"font.size": 12})

fig, ax = plt.subplots()

aleaciones = ("c-Si", "a-Si", "c-Li15Si4", "a-Li15Si4")

for aleacion in aleaciones:
    dataset = pd.read_csv(f"datasets/gofr-{aleacion}.csv")
    ax.plot(dataset.r, dataset.gofr, label=aleacion)

ax.set_xlim((2, 5.5))
ax.set_xlabel(r"r ($\AA$)")

ax.set_ylabel(r"G(r) ($\AA^{-2}$)")
ax.set_ylim((-4.9, 18))

ax.legend()

fig.tight_layout()
plt.savefig("gofrs.png", dpi=600)
