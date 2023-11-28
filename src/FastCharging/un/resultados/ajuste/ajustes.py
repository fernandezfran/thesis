#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2024, Francisco Fernandez
# License: CC BY-SA 4.0
#   https://github.com/fernandezfran/thesis/blob/main/LICENSE
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import galpynostatic

plt.rcParams.update({'font.size': 12})

path = "../data/"

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
abcdef = ["a", "b", "c", "d", "e", "f"]

fig, ax = plt.subplots(nrows=3, ncols=2, sharey=True, figsize=(7, 7))
ax = ax.ravel()

for i, (exp, sys, eq, maxdc, X, d, let) in enumerate(
    zip(experiments, systems, eq_pot, xmaxs, C_rates, lengths, abcdef)
):
    # preprocessing
    if exp == "mancini":
        df = pd.read_csv(f"{path}/{exp}.csv")

        X = np.array(df["crates"]).reshape(-1, 1)
        y = np.asarray(df["xmaxs"]) / maxdc

    else:
        dataframes = [pd.read_csv(f"{path}/{exp}/{x}C.csv", header=None) for x in X]

        dc = galpynostatic.preprocessing.GetDischargeCapacities(
            eq
        ).fit_transform(dataframes)

        X = np.array(X).reshape(-1, 1)
        y = dc / maxdc

    # model fitting
    greg = galpynostatic.model.GalvanostaticRegressor("spherical", d, 3)
    greg.fit(X, y)

    greg.plot.versus_data(
        X,
        y,
        ax=ax[i],
        data_kws={"linestyle": "", "label": "datos experimentales"},
        pred_kws={"label": "modelo"},
    )

    ax[i].set_ylabel("")
    ax[i].set_xlabel("")

    if i == 0:
        ax[i].legend(ncol=2, loc="upper right", bbox_to_anchor=(1.9, 1.3))
    if sys in ("LMO", "LNMO"):
        ax[i].set_xlabel("C-rates")
    if sys in ("NG", "LFP", "LMO"):
        ax[i].set_ylabel(r"SOC$_{max}$")

    ax[i].text(0.9, 0.9, f"({let})", transform=ax[i].transAxes)
    ax[i].text(0.05, 0.05, sys, transform=ax[i].transAxes)

fig.savefig("ajustes.png", dpi=600)
