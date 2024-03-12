#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2024, Francisco Fernandez
# License: CC BY-SA 4.0
#   https://github.com/fernandezfran/thesis/blob/main/LICENSE
import galpynostatic as gp
import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams.update({"font.size": 14})

df = pd.read_csv("../datasets/mancini.csv")

X, y = df["crates"].to_numpy().reshape(-1, 1), df["xmaxs"].to_numpy() / 100.0

reg = gp.model.GalvanostaticRegressor("spherical", 7.5e-4, 3)
reg.fit(X, y)

reg.plot.versus_data(
    X,
    y,
    data_kws={"linestyle": "", "label": "datos experimentales"},
    pred_kws={"linestyle": "--", "label": "modelo"},
)

plt.xlim((8e-2, 1.2e1))
plt.ylim((0.0, 1.0))

plt.xscale("log")
plt.xlabel("C-rate")
plt.ylabel(r"$SOC_{\max}$")
plt.legend()

plt.savefig("_socmax_vs_crate_plot.png", dpi=600)
plt.show()
