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


xvalues = np.logspace(-20, -8)
for tau, x, y in zip(np.logspace(7, -1, num=5), [0.54, 0.72, 0.9, 0.93, 0.93], [0.95, 0.95, 0.95, 0.77, 0.56]):
    ax1.plot(xvalues, tau * xvalues, color="tab:gray", linestyle="dashed", linewidth=1)
    exp = np.log10(tau)
    txt = fr"10$^{exp:.0f}$" if exp > 0 else f"{tau:.1f}"
    ax1.text(x, y, txt, c="tab:gray", transform=ax1.transAxes)

ax1.text(0.68, 0.17, r"Menor $\tau$ [s]", c="tab:gray", transform=ax1.transAxes)
ax1.text(0.68, 0.12, r"carga más", c="tab:gray", transform=ax1.transAxes)
ax1.text(0.68, 0.07, r"rápida de Xia", c="tab:gray", transform=ax1.transAxes)
ax1.text(0.68, 0.02, r"et al.", c="tab:gray", transform=ax1.transAxes)

ax1.arrow(0.76, 0.33, 0.1, -0.1, width=0.005, head_width=0.02, color="tab:gray", transform=ax1.transAxes)

ax1.set_xlim((7e-20, 1e-8))
ax1.set_xlabel(r"Coeficiente de difusión $D$ [m$^2$/s]")
ax1.set_xscale("log")

ax1.set_ylim((1e-15, 1e-6))
ax1.set_ylabel(r"Tamaño geométrico al cuadrado $d^2$ [$m^2$]")
ax1.set_yscale("log")

cmap = cm.get_cmap("viridis")
sm = plt.cm.ScalarMappable(cmap=cmap)
clb = fig.colorbar(sm, ax=ax1, location="right")
clb.ax.set_ylabel("UMBEM")

for sys, dcoeff, d in zip(df["Material"], df["dcoeff_midpoint_cm2s"], df["d_mean_micro"]):
    greg = galpynostatic.model.GalvanostaticRegressor(dataset, 1e-4 * d, 3)
    greg._map = galpynostatic.datasets.map.MapSpline(dataset)
    greg.dcoeff_, greg.k0_ = dcoeff, k0
    soc = greg.predict(np.array([[4.0]]))[0]
    soc = soc if ~np.isnan(soc) else 0.0
    socs[sys].append(soc)


    ax1.scatter(
        1e-4 * dcoeff,
        (1e-6 * d)**2,
        marker=marker[sys],
        color=cmap(soc),
        edgecolor="k",
    )

    soc = soc if ~np.isnan(soc) else 0.0
    tau = ((1e-6 * d)**2) / (1e-4 * dcoeff)
    ax2.scatter(tau, soc, color=cmap(soc), marker=marker[sys], edgecolor="k")

for sys in systems:
    print(np.mean(socs[sys]))
    ax2.scatter(0, 0, color=cmap(np.mean(socs[sys])), marker=marker[sys], label=sys, edgecolor="k")
ax2.legend(frameon=False)

ax2.axhline(y=0.8, color="tab:gray", linestyle="dashed", linewidth=1)

ax2.set_xscale("log")
ax2.set_xlim((0.1, 1e7))
ax2.set_xlabel("FOM")

ax2.set_ylim((0, 1))
ax2.set_ylabel("UMBEM")

plt.savefig("xiacomp.png", dpi=600)
plt.show()
