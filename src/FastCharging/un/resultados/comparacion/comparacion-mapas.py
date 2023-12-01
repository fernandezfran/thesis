#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2024, Francisco Fernandez
# License: CC BY-SA 4.0
#   https://github.com/fernandezfran/thesis/blob/main/LICENSE
from shared import *

for i, d in enumerate(dvalues):
    fig, ax = plt.subplots()

    models[0].plot.render_map(ax=ax, clb_label="valor máximo del SOC")

    for sys, greg, color in zip(systems, models, colors):
        greg.d = d

        ells = galpynostatic.utils.logell(crates, d, 3, greg.dcoeff_)
        xis = galpynostatic.utils.logxi(crates, greg.dcoeff_, greg.k0_)

        ax.plot(ells, xis, color=color, label=sys)

    ax.set_xlim((-4, 1.75))
    ax.set_ylim((-3.5, 2))

    fig.tight_layout()
    fig.savefig(f"comparacion-mapa{i}.png", dpi=600)
