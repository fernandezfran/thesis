#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2024, Francisco Fernandez
# License: CC BY-SA 4.0
#   https://github.com/fernandezfran/thesis/blob/main/LICENSE
import galpynostatic
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
import pandas as pd
import scipy.stats

plt.rcParams.update({'font.size': 12})

k0 = 1e-7

df = pd.read_csv("datasets/experimental_data.csv")

df["d_mean_micro"] = df["particle_size_micro"].str.split("-").apply(
    lambda x: np.mean([float(i) for i in x])
    if isinstance(x, list)
    else np.nan
)

df["d_mean_micro"] = df.groupby(
    "Material", group_keys=False
)["d_mean_micro"].apply(lambda x: x.fillna(x.mean()))

df["dcoeff_midpoint_cm2s"] = df["dcoeff_cm2s"].str.split(" to ").apply(
    lambda x: scipy.stats.gmean([float(i) for i in x])
)

systems = ("LCO", "LMO", "LTO", "LFP", "Ternarios", "Grafito")

marker, color, socs, opss, taus = {}, {}, {}, {}, {}
for sys, m, c in zip(systems, ("s", "o", "D", "^", "v", "<"), (None, "red", "pink", "blue", "green", "orange")):
    marker[sys] = m
    color[sys] = f"tab:{c}" if c is not None else "k"
    socs[sys], opss[sys], taus[sys] = [], [], []

dataset = pd.read_csv("datasets/simulated_spherical_map_200mV.csv")

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 5))

cmap = cm.get_cmap("viridis")

greg = galpynostatic.model.GalvanostaticRegressor(dataset, 1, 1)
greg._map = galpynostatic.datasets.map.MapSpline(dataset)
ax1 = greg.plot.render_map(ax=ax1, clb_label="UMBEM")

# contour line
X, Y = np.linspace(-5, 6), np.linspace(-5, 6)
Z = greg._map.soc(X, Y, grid=True).T
ax1.contour(X, Y, Z, levels=np.array([0.8]), colors="tab:gray", linewidths=1, linestyles="dashed")

X = np.array([[4.0]])
for sys, dcoeff, d in zip(df["Material"], df["dcoeff_midpoint_cm2s"], df["d_mean_micro"]):
    greg = galpynostatic.model.GalvanostaticRegressor(dataset, 1e-4 * d, 3)
    greg.dcoeff_, greg.k0_ = dcoeff, k0

    # greg.plot.in_render_map(X, ax=ax1, color=color[sys], marker=marker[sys], label="", linestyle="")
    logell = galpynostatic.utils.logell(X, 1e-4 * d, 3, dcoeff)
    logxi = galpynostatic.utils.logxi(X, dcoeff, k0)

    ax1.scatter(logell, logxi, marker=marker[sys], color=color[sys], edgecolor="k")

for sys in systems:
    ax1.scatter(-100, -100, color=color[sys], marker=marker[sys], label=sys, edgecolor="k")
ax1.legend(ncol=6, frameon=False, loc=(0.35, 1.05))

ax1.text(0, 1.05, "(a)", transform=ax1.transAxes)
ax2.text(0.95, 1.05, "(b)", transform=ax2.transAxes)

ax1.set_xlim((-4.25, 4.25))
ax1.set_ylim((-4, 4))

for sys, dcoeff, d in zip(df["Material"], df["dcoeff_midpoint_cm2s"], df["d_mean_micro"]):
    greg = galpynostatic.model.GalvanostaticRegressor(dataset, 1e-4 * d, 3)
    greg._map = galpynostatic.datasets.map.MapSpline(dataset)
    greg.dcoeff_, greg.k0_ = dcoeff, k0
    soc = greg.predict(np.array([[4.0]]))[0]
    soc = soc if ~np.isnan(soc) else 0.0
    socs[sys].append(soc)

ax2.axhline(y=0.8, color="tab:gray", linestyle="dashed", linewidth=1)

x = np.linspace(0, 1, num=len(socs.keys()))
w = 0.02
for i, v in enumerate(socs.values()):
    colors = [cmap(soc) for soc in v]
    xs = np.linspace(x[i] - (w / 2) * len(v), x[i] + (w / 2) * len(v), num=len(v))
    ax2.bar(xs, v, width=w, color=colors)

ax2.set_xticks(x)
ax2.set_xticklabels(socs.keys())
ax2.set_ylim((0, 1))
ax2.set_ylabel("UMBEM")

plt.savefig("UMBEM.png", dpi=600)
plt.show()
