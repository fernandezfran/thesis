#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

import itertools as it
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({'font.size': 16})

chi_values = (0.01, 1)
l_values = (0.0001, 0.001, 0.01, 0.1, 1, 10)
chill = it.product(chi_values, l_values)

files = os.popen("ls -l data/*.dat | awk '{print $9}'").read().split()

fig, ax = plt.subplots(nrows=2, ncols=1, sharex=True, figsize=(9.5, 6))

for file, (chi, l) in zip(files, chill):
    data = np.loadtxt(file, dtype=np.float32, skiprows=1, unpack=True)
    x, potential = data[0], data[2]

    ax[chi_values[::-1].index(chi)].plot(x, potential, label=f"{np.log10(l)}")

for a, chi, bc in zip(ax, chi_values[::-1], ["(b)", "(c)"]):
    a.text(0.025, 0.12, bc)
    a.text(0.78, 0.11, rf"log($\Xi$) = {np.log10(chi)}")
    a.set_ylabel("Potencial (V)")
    a.set_ylim((-0.15, 0.15))

    a.set_yticks([-0.1, 0.0, 0.1])

ax[1].set_xlabel("SOC")
ax[1].set_xlim((0, 1))

ax[0].legend(title=r"log($l$)", loc='center left', bbox_to_anchor=(1, 0.0))

fig.subplots_adjust(wspace=0, hspace=0, right=0.85)
# fig.tight_layout()
fig.savefig("plot.png", dpi=200)
