#!/usr/bin/env python
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from galpynostatic.datasets import load_spherical
from galpynostatic.model import GalvanostaticRegressor
from galpynostatic.preprocessing import GetDischargeCapacities

plt.rcParams.update({'font.size': 12})

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
abc = ["(i)", "(ii)", "(iii)"]
colors = ["tab:blue", "tab:orange", "tab:green", "tab:red", "tab:purple", "tab:pink"]

fig, ax = plt.subplots(nrows=3, ncols=1, sharex=True, figsize=(6, 7))
ax = ax.ravel()

dataset = load_spherical()


crates = np.logspace(-2, 2, num=200).reshape(-1, 1)
for i, (d, let) in enumerate(zip(dvalues, abc)):
    for exp, sys, eq, maxdc, X, length, color in zip(
        experiments, systems, eq_pot, xmaxs, C_rates, lengths, colors
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

        # ordenada = np.log10((greg.k0_ * greg.d) / (greg.dcoeff_ * np.sqrt(3)))
        # ells = np.arange(-4, 2, 0.1)
        # xis = ordenada - 0.5 * ells
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
