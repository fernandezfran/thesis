#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2024, Francisco Fernandez
# License: CC BY-SA 4.0
#   https://github.com/fernandezfran/thesis/blob/main/LICENSE
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

plt.rcParams.update({"font.size": 12})

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
    .apply(lambda x: np.mean([float(i) for i in x]))
)

systems = ("LCO", "LMO", "LTO", "LFP", "Ternarios", "Grafito")

marker, color = {}, {}
for sys, m, c in zip(
    systems,
    ("s", "o", "D", "^", "v", "<"),
    (None, "red", "pink", "blue", "green", "orange"),
):
    marker[sys] = m
    color[sys] = f"tab:{c}" if c is not None else "k"

fig, ax = plt.subplots()

xvalues = np.logspace(-20, -8)
for tau, x, y in zip(
    np.logspace(7, -1, num=5),
    [0.54, 0.72, 0.9, 0.93, 0.93],
    [0.95, 0.95, 0.95, 0.77, 0.56],
):
    ax.plot(xvalues, tau * xvalues, color="tab:gray", linestyle="dashed", linewidth=1)
    exp = np.log10(tau)
    txt = fr"10$^{exp:.0f}$" if exp > 0 else f"{tau:.1f}"
    ax.text(x, y, txt, c="tab:gray", transform=ax.transAxes)

ax.text(0.68, 0.17, r"Menor $\tau$ [s]", c="tab:gray", transform=ax.transAxes)
ax.text(0.68, 0.12, r"carga más", c="tab:gray", transform=ax.transAxes)
ax.text(0.68, 0.07, r"rápida de Xia", c="tab:gray", transform=ax.transAxes)
ax.text(0.68, 0.02, r"et al.", c="tab:gray", transform=ax.transAxes)

ax.arrow(
    0.76,
    0.33,
    0.1,
    -0.1,
    width=0.005,
    head_width=0.02,
    color="tab:gray",
    transform=ax.transAxes,
)

ax.set_xlim((7e-20, 1e-8))
ax.set_xlabel(r"Coeficiente de difusión $D$ [m$^2$/s]")
ax.set_xscale("log")

ax.set_ylim((1e-15, 1e-6))
ax.set_ylabel(r"Tamaño geométrico al cuadrado $d^2$ [$m^2$]")
ax.set_yscale("log")

for sys, dcoeff, d in zip(
    dataset["Material"], dataset["dcoeff_midpoint_cm2s"], dataset["d_mean_micro"]
):
    ax.scatter(
        1e-4 * dcoeff,
        (1e-6 * d) ** 2,
        marker=marker[sys],
        color=color[sys],
        edgecolor="k",
    )

for sys in systems:
    ax.scatter(0, 0, color=color[sys], marker=marker[sys], label=sys, edgecolor="k")
ax.legend(frameon=False)

fig.tight_layout()
fig.savefig("xiafom.png", dpi=600)
