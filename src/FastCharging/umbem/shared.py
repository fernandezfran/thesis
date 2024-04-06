#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2024, Francisco Fernandez
# License: CC BY-SA 4.0
#   https://github.com/fernandezfran/thesis/blob/main/LICENSE
import galpynostatic
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.stats

plt.rcParams.update({"font.size": 12})
cmap = plt.colormaps["viridis"]

dataset = pd.read_csv("datasets/experimental_data.csv")

dataset["d_mean_micro"] = (
    dataset["particle_size_micro"]
    .str.split("-")
    .apply(lambda x: np.mean([float(i) for i in x]) if isinstance(x, list) else np.nan)
)

dataset["d_mean_micro"] = dataset.groupby("Material", group_keys=False)[
    "d_mean_micro"
].apply(lambda x: x.fillna(x.mean()))

dataset["dcoeff_midpoint_cm2s"] = (
    dataset["dcoeff_cm2s"]
    .str.split(" to ")
    .apply(lambda x: scipy.stats.gmean([float(i) for i in x]))
)

spherical = pd.read_csv("datasets/simulated_spherical_map_200mV.csv")

k0 = 1e-7

systems = ("LCO", "LMO", "LTO", "LFP", "Ternarios", "Grafito")

marker, color, socs, opss, = (
    {},
    {},
    {},
    {},
)
for sys, m, c in zip(
    systems,
    ("s", "o", "D", "^", "v", "<"),
    (None, "red", "pink", "blue", "green", "orange"),
):
    marker[sys] = m
    color[sys] = f"tab:{c}" if c is not None else "k"
    socs[sys], opss[sys] = [], []

for i, (sys, dcoeff, d) in enumerate(
    zip(dataset["Material"], dataset["dcoeff_midpoint_cm2s"], dataset["d_mean_micro"])
):
    greg = galpynostatic.model.GalvanostaticRegressor(spherical, 1e-4 * d, 3)
    greg._map = galpynostatic.base.MapSpline(spherical)
    greg.dcoeff_, greg.k0_ = dcoeff, k0
    greg.dcoeff_err_ = None
    soc = greg.predict(np.array([[4.0]]))[0]
    soc = soc if ~np.isnan(soc) else 0.0
    socs[sys].append(soc)

    # size predictions
    d0 = 1e-5 * d
    if i in [5, 24, 30]:
        d0 = 10.0 * d0
    elif i in [11, 12, 13, 14]:
        d0 = 1e-4 * d
    elif i == 23:
        d0 = 0.3 * d0

    try:
        ops = galpynostatic.make_prediction.optimal_particle_size(greg, d0=d0)
    except ValueError as e:
        num = 100
        if i in [22, 24]:
            num = 1000
        elif i in [12, 14]:
            num = 225

        loggrid = np.logspace(-7, -4, num=num)
        for d0 in loggrid:
            try:
                ops = galpynostatic.make_prediction.optimal_particle_size(greg, d0=d0)
                break
            except ValueError as e:
                ...
    finally:
        opss[sys].append(ops / d)
