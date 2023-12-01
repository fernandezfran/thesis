#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2024, Francisco Fernandez
# License: CC BY-SA 4.0
#   https://github.com/fernandezfran/thesis/blob/main/LICENSE
import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams.update({"font.size": 16})

fig, ax = plt.subplots(ncols=2, figsize=(13, 5))

cristales = pd.read_csv("datasets/cristales.csv")

ax[0].plot(
    cristales.x,
    1e-2 * cristales.A0,
    color="tab:blue",
    ls="dashed",
    label=r"DFTB conjunto A$_0$",
)
ax[0].plot(
    cristales.x,
    1e-2 * cristales.A,
    color="tab:blue",
    ls="solid",
    label=r"DFTB conjunto A",
)
ax[0].plot(
    cristales.x,
    1e-2 * cristales.B0,
    color="tab:green",
    ls="dashed",
    label=r"DFTB conjunto B$_0$",
)
ax[0].plot(
    cristales.x,
    1e-2 * cristales.B,
    color="tab:green",
    ls="solid",
    label=r"DFTB conjunto B",
)

ax[0].set_xlim((0, 1))
ax[0].set_xlabel("Fracción molar de Si")

ax[0].set_ylim((0, 9e-2))
ax[0].set_ylabel(r"|$F^{DFT}$ - $F^{DFTB}$| (eV)")

ax[0].text(0.0, 1.05, "(a)", transform=ax[0].transAxes)

ax[0].legend()

amorfosa = pd.read_csv("datasets/amorfos-A.csv")

ax[1].plot(
    amorfosa.x, amorfosa.A0, color="tab:blue", ls="dashed", label=r"DFTB conjunto A$_0$"
)
ax[1].plot(
    amorfosa.x, amorfosa.A, color="tab:blue", ls="solid", label=r"DFTB conjunto A"
)

amorfosb = pd.read_csv("datasets/amorfos-B.csv")

ax[1].plot(
    amorfosb.x,
    amorfosb.B0,
    color="tab:green",
    ls="dashed",
    label=r"DFTB conjunto B$_0$",
)
ax[1].plot(
    amorfosb.x, amorfosb.B, color="tab:green", ls="solid", label=r"DFTB conjunto B"
)

ax[1].set_xlim((0.19, 1))
ax[1].set_xlabel("Fracción molar de Si")

ax[1].set_ylim((0, 0.2))
ax[1].set_yticks([0, 0.05, 0.1, 0.15, 0.2])

ax[1].text(0.92, 1.05, "(b)", transform=ax[1].transAxes)

fig.tight_layout()
fig.savefig("residuos.png", dpi=600)
