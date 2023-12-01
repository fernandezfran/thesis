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

abcdef = ["a", "b", "c", "d", "e", "f"]
markers = ["o", "v", "^", ">", "<", "s"]
colors = ["tab:" + c for c in ("blue", "orange", "green", "red", "purple", "pink")]

systems = ["NG", "LTO", "LFP", "LCO", "LMO", "LNMO"]

experiments = ["mancini", "he", "lei", "wang", "bak", "nishikawa"]
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
lengths = [7.5e-4, 1.75e-4, 3.5e-5, 2e-3, 2.5e-6, np.sqrt(8.04e-6 / 4 /np.pi)]

X_data, y_data, models = [], [], []
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

    X_data.append(X)
    y_data.append(y)

    greg = galpynostatic.model.GalvanostaticRegressor("spherical", d, 3)
    greg.fit(X, y)

    models.append(greg)
