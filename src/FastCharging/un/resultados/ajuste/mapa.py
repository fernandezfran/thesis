#!/usr/bin/env python
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from galpynostatic.datasets import load_spherical
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
    [2.5, 5.0, 7.5, 12.5, 25.]
]
lengths = [0.00075, 0.000175, 3.5e-5, 0.002, 2.5e-6, np.sqrt(0.25 * 8.04e-6 / np.pi)]
markers = ["o", "v", "^", ">", "<", "s"]
colors = ["tab:blue", "tab:orange", "tab:green", "tab:red", "tab:purple", "tab:pink"]

fig, ax = plt.subplots()

dataset = load_spherical()

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

    ax.plot(logell(X, d, 3, greg.dcoeff_), logxi(X, greg.dcoeff_, greg.k0_), color="k", linestyle="--")
    ax.scatter(logell(X, d, 3, greg.dcoeff_), logxi(X, greg.dcoeff_, greg.k0_), marker=m, label=sys, color=c, edgecolors="k")

ax.set_xlabel(r"log ($\ell$)")
ax.set_ylabel(r"log ($\Xi$)")
ax.legend()

fig.tight_layout()
fig.savefig("mapa.png", dpi=600)
