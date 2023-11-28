#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2024, Francisco Fernandez
# License: CC BY-SA 4.0
#   https://github.com/fernandezfran/thesis/blob/main/LICENSE
import galpynostatic
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.metrics import r2_score

plt.rcParams.update({"font.size": 12})

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
markers = ["o", "v", "^", ">", "<", "s"]
colors = ["tab:blue", "tab:orange", "tab:green", "tab:red", "tab:purple", "tab:pink"]

dataset = galpynostatic.datasets.load_spherical()

fig, ax = plt.subplots()

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

        dc = galpynostatic.preprocessing.GetDischargeCapacities(eq).fit_transform(
            dataframes
        )

        X = np.array(X).reshape(-1, 1)
        y = dc / maxdc

    # model fitting
    greg = galpynostatic.model.GalvanostaticRegressor(dataset, d, 3)
    greg.fit(X, y)
    ypred = greg.predict(X)

    ax.scatter(
        y,
        ypred,
        marker=m,
        color=c,
        alpha=0.75,
        label=f"{sys}: {r2_score(y, ypred):.3f}",
    )

ax.plot([-0.1, 1.1], [-0.1, 1.1], ls="dashed", c="tab:gray", alpha=0.75)

ax.set_xlabel(r"Valor experimental de SOC$_{max}$")
ax.set_ylabel(r"Predicción de SOC$_{max}$")

ax.set_xlim((0.05, 1.05))
ax.set_ylim((0.05, 1.05))

ax.legend(title="R$^2$")

fig.savefig("pred_vs_exp.png", dpi=600)
