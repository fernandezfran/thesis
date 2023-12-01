#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2024, Francisco Fernandez
# License: CC BY-SA 4.0
#   https://github.com/fernandezfran/thesis/blob/main/LICENSE
import galpynostatic
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

plt.rcParams.update({"font.size": 12})

experiments = ["mancini", "he", "lei", "wang", "bak", "nishikawa"]
systems = ["NG", "LTO", "LFP", "LCO", "LMO", "LNMO"]
eq_pot = [None, 1.57, 3.45, 3.9, 4.0, 4.739]
xmaxs = [100, 160, 168.9, 100, 132.4, 0.38]
C_rates = [
    None,
    [0.1, 0.5, 1, 2, 5],
    [0.2, 0.5, 1, 2, 5, 10],
    [0.5, 1, 2, 5, 10, 20],
    [1, 5, 10, 20, 50, 100],
    [2.5, 5.0, 7.5, 12.5, 25.0],
]
lengths = [7.5e-4, 1.75e-4, 3.5e-5, 2e-3, 2.5e-6, np.sqrt(8.04e-6 / 4 / np.pi)]
markers = ["o", "v", "^", ">", "<", "s"]
colors = ["tab:" + c for c in ("blue", "orange", "green", "red", "purple", "pink")]

fig, ax = plt.subplots()

models = []
for exp, eq, maxdc, X, d in zip(experiments, eq_pot, xmaxs, C_rates, lengths):
    if exp == "mancini":
        df = pd.read_csv(f"../datasets/{exp}.csv")

        X = np.array(df["crates"]).reshape(-1, 1)
        y = np.asarray(df["xmaxs"]) / maxdc
    else:
        dataframes = [
            pd.read_csv(f"../datasets/{exp}/{x}C.csv", header=None) for x in X
        ]

        dc = galpynostatic.preprocessing.GetDischargeCapacities(eq).fit_transform(
            dataframes
        )

        X = np.array(X).reshape(-1, 1)
        y = dc / maxdc

    greg = galpynostatic.model.GalvanostaticRegressor("spherical", d, 3)
    greg.fit(X, y)

    models.append(greg)

greg.plot.render_map(ax=ax, clb_label="valor máximo del SOC")
cuatroc = np.array([4])

arrow_from, crosses = [], []
for greg in models:
    ell = galpynostatic.utils.logell(cuatroc, greg.d, 3, greg.dcoeff_)
    xi = galpynostatic.utils.logxi(cuatroc, greg.dcoeff_, greg.k0_)

    arrow_from.append([ell[0], xi[0]])

    greg.d, _ = galpynostatic.make_prediction.optimal_particle_size(greg, cm_to=1)
    new_ell = galpynostatic.utils.logell(cuatroc, greg.d, 3, greg.dcoeff_)

    crosses.append([new_ell[0], xi[0]])

X = np.linspace(-4, 1.75, num=100)
Y = np.linspace(-3.5, 2, num=100)
Z = greg._map.soc(X, Y, grid=True).T
ax.contour(X, Y, Z, levels=np.array([0.8]), colors="red")

dg = 0.1
for cross, arrow, sys, m, c in zip(crosses, arrow_from, systems, markers, colors):
    ax.scatter(cross[0], cross[1], color="red", marker="x")

    dx, dy = cross[0] - arrow[0], cross[1] - arrow[1]
    dx = dx - 2.0 * dg if dx > 0 else dx + 2.0 * dg
    ax.arrow(
        arrow[0], arrow[1], dx, dy, fc="k", head_width=dg, head_length=dg, overhang=1
    )

    ax.scatter(arrow[0], arrow[1], marker=m, label=sys, color=c, edgecolors="k")

ax.set_xlabel(r"log ($\ell$)")
ax.set_ylabel(r"log ($\Xi$)")
ax.legend(loc="upper left")

fig.tight_layout()
fig.savefig("prediccion.png", dpi=600)
