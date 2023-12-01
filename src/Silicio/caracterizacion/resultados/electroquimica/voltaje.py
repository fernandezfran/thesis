#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2024, Francisco Fernandez
# License: CC BY-SA 4.0
#   https://github.com/fernandezfran/thesis/blob/main/LICENSE
import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams.update({"font.size": 12})

fig, ax = plt.subplots()

dataset_fe = pd.read_csv(
    "datasets/voltaje/fe.dat", delimiter=" ", comment="#", names=["xfe", "fe", "dfe"]
)
dataset_fe_spline = pd.read_csv(
    "datasets/voltaje/fe-spline.dat", delimiter=" ", comment="#", names=["x", "fe", "v"]
)
dataset_dft = pd.read_csv("datasets/voltaje/v-chev.csv")
dataset_exp1 = pd.read_csv("datasets/voltaje/v1-exp.dat")
dataset_exp2 = pd.read_csv("datasets/voltaje/v2-exp.dat")

ax.plot(dataset_exp1.x, dataset_exp1.v, color="tab:blue", label="a-Si")
ax.plot(dataset_exp2.x, dataset_exp2.v, color="tab:blue")
ax.plot(dataset_dft.x, dataset_dft.v, color="k", label="DFT spline")
ax.plot(
    dataset_fe_spline.x, dataset_fe_spline.v, color="tab:orange", label="ReaxFF spline"
)

ax.set_xlim((0, 4.25))
ax.set_xlabel(r"$x$ en Li$_x$Si")
ax.secondary_xaxis(
    "top", functions=(lambda x: 4056.2 * x / 4.25, lambda x: 4056.2 * x / 4.25)
).set_xlabel(r"Capacidad (mAhg$^{-1}$)")

ax.set_ylim((-0.01, 0.8))
ax.set_ylabel(r"Voltaje (V vs Li/Li$^+$)")

ax.legend(loc=3)

# formation energy inset
fontsize = 8

left, bottom, width, height = [0.55, 0.529, 0.35, 0.35]
ax2 = fig.add_axes([left, bottom, width, height])

ax2.scatter(dataset_fe.xfe, dataset_fe.fe, color="k", marker="s", s=15, label="ReaxFF")
ax2.plot(dataset_fe_spline.x, dataset_fe_spline.fe, color="tab:orange", label="spline")

ax2.set_xlim((0, 4.25))
ax2.set_xlabel(r"$x$ en Li$_x$Si", fontsize=fontsize)

ax2.tick_params(axis="both", which="major", labelsize=fontsize)

ax2.set_ylim((-0.745, 0.575))
ax2.set_ylabel("Energía de formación (eV)", fontsize=fontsize)

ax2.legend(prop={"size": fontsize})

fig.savefig("voltaje.png", dpi=600)
