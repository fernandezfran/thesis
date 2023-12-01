#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2024, Francisco Fernandez
# License: CC BY-SA 4.0
#   https://github.com/fernandezfran/thesis/blob/main/LICENSE
from shared import *

fig, ax = plt.subplots()

models[0].plot.render_map(ax=ax, clb_label="valor máximo del SOC")

for sys, greg, X, m, c in zip(systems, models, X_data, markers, colors):
    logell = galpynostatic.utils.logell(X, greg.d, 3, greg.dcoeff_)
    logxi = galpynostatic.utils.logxi(X, greg.dcoeff_, greg.k0_)

    ax.plot(logell, logxi, color="k", linestyle="--")
    ax.scatter(logell, logxi, marker=m, label=sys, color=c, edgecolors="k")

ax.set_xlabel(r"log ($\ell$)")
ax.set_ylabel(r"log ($\Xi$)")
ax.legend()

fig.tight_layout()
fig.savefig("mapa.png", dpi=600)
