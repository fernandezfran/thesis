#!/usr/bin/env python
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from galpynostatic.datasets import load_spherical
from galpynostatic.make_prediction import optimal_particle_size
from galpynostatic.model import GalvanostaticRegressor
from galpynostatic.preprocessing import GetDischargeCapacities
from galpynostatic.utils import logell, logxi

plt.rcParams.update({"font.size": 12})

path = "../data"

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
lengths = [0.00075, 0.000175, 3.5e-5, 0.002, 2.5e-6, np.sqrt(0.25 * 8.04e-6 / np.pi)]
markers = ["o", "v", "^", ">", "<", "s"]
colors = ["tab:blue", "tab:orange", "tab:green", "tab:red", "tab:purple", "tab:pink"]

fig, ax = plt.subplots()

dataset = load_spherical()

arrow_from, crosses = [], []
for i, (exp, sys, eq, maxdc, X, d, m, c) in enumerate(
    zip(experiments, systems, eq_pot, xmaxs, C_rates, lengths, markers, colors)
):
    # preprocessing
    if exp == "mancini":
        df = pd.read_csv(f"{path}/{exp}.csv")

        X = np.array(df["crates"]).reshape(-1, 1)
        y = np.asarray(df["xmaxs"]) / maxdc

    else:
        dataframes = [pd.read_csv(f"{path}/{exp}/{x}C.csv", header=None) for x in X]

        dc = GetDischargeCapacities(eq).fit_transform(dataframes)

        X = np.array(X).reshape(-1, 1)
        y = dc / maxdc

    # model fitting
    greg = GalvanostaticRegressor(dataset, d, 3)
    greg.fit(X, y)

    if i == 0:
        greg.plot.render_map(ax=ax, clb_label="valor máximo del SOC")

    cuatroc = np.array([4])
    ell, xi = logell(cuatroc, d, 3, greg.dcoeff_), logxi(
        cuatroc, greg.dcoeff_, greg.k0_
    )
    arrow_from.append([ell[0], xi[0]])

    # to define the crosses points at 4 C and 0.8 of SOC
    greg.d, _ = optimal_particle_size(greg, cm_to=1)
    new_ell = logell(cuatroc, greg.d, 3, greg.dcoeff_)

    crosses.append([new_ell[0], xi[0]])

# 0.8 soc contour
X = np.linspace(-4, 1.75, num=100)
Y = np.linspace(-3.5, 2, num=100)
Z = greg._map.soc(X, Y, grid=True).T

ax.contour(X, Y, Z, levels=np.array([0.8]), colors="red")

# crosses & arrows & scatters
for cross, arrow, sys, m, c in zip(crosses, arrow_from, systems, markers, colors):
    ax.scatter(cross[0], cross[1], color="red", marker="x")

    dx = cross[0] - arrow[0]
    delta = 0.1
    ax.arrow(
        arrow[0],
        arrow[1],
        dx - 2.0 * delta if dx > 0 else dx + 2.0 * delta,
        cross[1] - arrow[1],
        fc="k",
        head_width=delta,
        head_length=delta,
        overhang=1,
    )

    ax.scatter(arrow[0], arrow[1], marker=m, label=sys, color=c, edgecolors="k")

# ax.text(-3.9, -2.25, "Zona de carga rápida", rotation=27.5)
# ax.text(-3.5, -3.25, "Zona de no-carga rápida", rotation=27.5, color="white")

ax.set_xlabel(r"log ($\ell$)")
ax.set_ylabel(r"log ($\Xi$)")
ax.legend(loc="upper left")

# fig.tight_layout()
fig.savefig("prediccion.png", dpi=600)
