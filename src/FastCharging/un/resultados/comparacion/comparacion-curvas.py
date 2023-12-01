#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2024, Francisco Fernandez
# License: CC BY-SA 4.0
#   https://github.com/fernandezfran/thesis/blob/main/LICENSE
from shared import *

fig, ax = plt.subplots(nrows=3, ncols=1, sharex=True, figsize=(6, 7))
ax = ax.ravel()

abc = ["(i)", "(ii)", "(iii)"]

for i, (d, let) in enumerate(zip(dvalues, abc)):
    for sys, greg, color in zip(systems, models, colors):
        greg.d = d
        socs = greg.predict(crates)

        ax[i].plot(crates, socs, color=color, label=sys)

        ax[i].text(1e-2, 1.05, rf"d={10000 * d}$\mu$m")
        ax[i].text(60, 1.05, let)

        ax[i].set_xscale("log")
        ax[i].set_xlim((1e-2, 1e2))

        ax[i].set_ylim(0, 1)
        ax[i].set_ylabel(r"SOC$_{max}$")

ax[0].text(2.5e-3, 1.2, "(a)")
ax[0].text(2e2, 1.2, "(b)")
ax[0].legend(prop={"size": 11})
ax[2].set_xlabel("C-rate")

fig.savefig("comparacion-curvas.png", dpi=600)
