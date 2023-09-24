#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams.update({"font.size": 16})

fig, ax = plt.subplots(ncols=2, figsize=(13, 5))

cristales = pd.read_csv("datos/cristales.csv")

ax[0].plot(cristales.x, cristales.dft, color="k", marker="o", ls="--", label="DFT")
ax[0].plot(
    cristales.x, cristales.reax, color="tab:orange", marker="x", ls="--", label="ReaxFF"
)
ax[0].plot(
    cristales.x,
    cristales.dftba,
    color="tab:blue",
    marker="^",
    ls="--",
    label="DFTB conjunto A",
)
ax[0].plot(
    cristales.x,
    cristales.dftbb,
    color="tab:green",
    marker="v",
    ls="--",
    label="DFTB conjunto B",
)

ax[0].set_xlim((0, 1))
ax[0].set_xlabel("Fracción molar de Si")
ax[0].set_ylim((-0.32, 0.05))
ax[0].set_ylabel("Energía de formación (eV)")

ax[0].text(0.0, 1.05, "(a)", transform=ax[0].transAxes)

ax[0].legend(ncol=4, bbox_to_anchor=(2.1, 1.15))

ax[1].plot(cristales.x, cristales.dft, color="k", marker="o", ls="--", alpha=0.25)
amorfos = pd.read_csv("datos/amorfos.csv")
ax[1].plot(amorfos.x, amorfos.dft, color="k", marker="o", ls="--")
ax[1].plot(amorfos.x, amorfos.reax, color="tab:orange", marker="x", ls="--")
ax[1].plot(amorfos.x, amorfos.dftba, color="tab:blue", marker="^", ls="--")
ax[1].plot(amorfos.x, amorfos.dftbb, color="tab:green", marker="v", ls="--")

ax[1].set_xlim((0, 1))
ax[1].set_xlabel("Fracción molar de Si")
ax[1].set_ylim((-0.37, 0.84))

ax[1].text(0.92, 1.05, "(b)", transform=ax[1].transAxes)

fig.savefig("energias.png", dpi=600)
