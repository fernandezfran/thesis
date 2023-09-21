#!/usr/bin/env python
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

plt.rcParams.update({'font.size': 12})

path = "../data/wang"

C_rates = [0.5, 1, 2, 5, 10, 20]
dataframes = [pd.read_csv(f"{path}/{crate}C.csv", header=None) for crate in C_rates]

eq_pot = 3.9
vcut = 0.15

fig, ax = plt.subplots()

for crate, df in zip(C_rates, dataframes):
    ax.plot(df[0] / 100, df[1], label=f"{crate}")

dtext = 0.01

ax.axhline(y=eq_pot, color="k", linestyle="--")
ax.text(0 + dtext, eq_pot + dtext, r"$E^0$")

ax.axhline(y=eq_pot - vcut, color="k", linestyle="--")
ax.text(0 + dtext, eq_pot - vcut + dtext, r"$E^0 - E_{off}$")

ax.set_xlim((0, 1))
ax.set_ylim((3.5, 4.4))
ax.set_xlabel(r"SOC")
ax.set_ylabel(r"Potencial (V vs. Li$^+$/Li)")
ax.legend(title="C-rate")
fig.savefig("preprocesamiento.png", dpi=600)
plt.show()
