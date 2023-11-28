#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2024, Francisco Fernandez
# License: CC BY-SA 4.0
#   https://github.com/fernandezfran/thesis/blob/main/LICENSE
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from galpynostatic.datasets import load_spherical
from galpynostatic.model import GalvanostaticRegressor
from galpynostatic.preprocessing import GetDischargeCapacities
from galpynostatic.utils import logell, logxi


plt.rcParams.update({'font.size': 22})

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
dvalues = [1e-5, 1e-4, 0.001]
colors = ["tab:blue", "tab:orange", "tab:green", "tab:red", "tab:purple", "tab:pink"]

dataset = load_spherical()

crates = np.logspace(-2, 2, num=200).reshape(-1, 1)
for i, d in enumerate(dvalues):

    fig, ax = plt.subplots()
    for j, (exp, sys, eq, maxdc, X, length, color) in enumerate(
        zip(experiments, systems, eq_pot, xmaxs, C_rates, lengths, colors)
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
        greg = GalvanostaticRegressor(dataset, length, 3)
        greg.fit(X, y)

        greg.d = d

        ells = np.array([logell(cr[0], d, 3, greg.dcoeff_) for cr in crates])
        xis = np.array([logxi(cr[0], greg.dcoeff_, greg.k0_) for cr in crates])

        if j == 0:
            greg.plot.render_map(ax=ax, clb_label="valor máximo del SOC")

        ax.plot(ells, xis, color=color, label=sys)

    # ax.text(-4, 2.2, rf"d={d*10000}$\mu$m")

    ax.set_xlim((-4, 1.75))
    ax.set_ylim((-3.5, 2))

    fig.tight_layout()
    fig.savefig(f"comparacion-mapa{i}.png", dpi=600)
