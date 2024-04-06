#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2024, Francisco Fernandez
# License: CC BY-SA 4.0
#   https://github.com/fernandezfran/thesis/blob/main/LICENSE
import os

import itertools as it
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({"font.size": 16})

xi_values = (0.01, 1)
ell_values = (0.0001, 0.001, 0.01, 0.1, 1, 10)
chill = it.product(xi_values, ell_values)

files = os.popen("ls -l datasets/*.dat | awk '{print $9}'").read().split()

fig, ax = plt.subplots(nrows=2, ncols=1, sharex=True, figsize=(9.5, 6))

for i, (file, (xi, ell)) in enumerate(zip(files, chill)):
    dataset = np.loadtxt(file, dtype=np.float32, skiprows=1, unpack=True)
    x, potential = dataset[0], dataset[2]
    j = 0 if i < 6 else 1

    ax[j].plot(x, potential, label=f"{np.log10(ell)}", zorder=1)
    ax[j].scatter(x[-1], -0.15, s=150, marker="^", color="k", zorder=2)

for a, xi, bc in zip(ax, xi_values[::-1], ["(b)", "(c)"]):
    a.text(0.025, 0.12, bc)
    a.text(0.78, 0.11, rf"log($\Xi$) = {np.log10(xi)}")
    a.set_ylabel("Potencial (V)")
    a.set_ylim((-0.15, 0.15))
    a.set_yticks([-0.1, 0.0, 0.1])

ax[1].set_xlabel("SOC")
ax[1].set_xlim((0, 1))

ax[0].legend(title=r"log($\ell$)", loc="center left", bbox_to_anchor=(1, 0.0))

fig.subplots_adjust(wspace=0, hspace=0, right=0.85)
fig.savefig("plot.png", dpi=200)
