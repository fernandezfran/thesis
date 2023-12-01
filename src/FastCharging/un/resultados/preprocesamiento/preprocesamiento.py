#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2024, Francisco Fernandez
# License: CC BY-SA 4.0
#   https://github.com/fernandezfran/thesis/blob/main/LICENSE
import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams.update({"font.size": 12})

eq_pot, vcut = 3.9, 0.15
C_rates = [0.5, 1, 2, 5, 10, 20]
dfs = [pd.read_csv(f"../datasets/wang/{cr}C.csv", header=None) for cr in C_rates]

fig, ax = plt.subplots()

for crate, df in zip(C_rates, dfs):
    ax.plot(df[0] / 100, df[1], label=f"{crate}")

dtext = 0.01
ax.axhline(y=eq_pot, color="k", linestyle="--")
ax.text(0 + dtext, eq_pot + dtext, r"$E^0$")
ax.axhline(y=eq_pot - vcut, color="k", linestyle="--")
ax.text(0 + dtext, eq_pot - vcut + dtext, r"$E^0 - E_{off}$")

ax.set_xlim((0, 1))
ax.set_xlabel(r"SOC")

ax.set_ylabel(r"Potencial (V vs. Li$^+$/Li)")
ax.set_ylim((3.5, 4.4))

ax.legend(title="C-rate")

fig.tight_layout()
fig.savefig("preprocesamiento.png", dpi=600)
