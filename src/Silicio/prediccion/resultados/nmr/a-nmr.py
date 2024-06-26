#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2024, Francisco Fernandez
# License: CC BY-SA 4.0
#   https://github.com/fernandezfran/thesis/blob/main/LICENSE
import matplotlib.pyplot as plt
import pandas as pd

fig, ax = plt.subplots()

plt.rcParams.update({"font.size": 12})

xvals = [0.20, 0.56, 0.89, 2.00, 3.28, 3.75][::-1]
voltajes = ["000", "050", "085", "095", "100", "105"]
for x, volt in zip(xvals, voltajes):
    dataset = pd.read_csv(f"datasets/{volt}.csv")

    ax.scatter(dataset.ppm, dataset.exp, s=5, color="k", zorder=2)
    ax.plot(dataset.ppm, dataset.pred, color="tab:blue", linewidth=3, zorder=1)

    ax.text(-20, 0.3 + dataset.exp[0], f"{volt} mV ~ x={x:.2f}")

ax.text(35, 11.2, "Si enlazados")
ax.vlines(18.0, 0, 11, color="k", linestyles="dashed")

ax.text(16, 11.2, "Si aislados")
ax.vlines(6.0, 0, 11, color="k", linestyles="dashed")

ax.text(-0.3, 11.2, "SEI")
ax.vlines(-0.3, 0, 11, color="k", linestyles="dashed")

ax.set_xlim((50, -50))
ax.set_xlabel(r"$\delta$ (ppm)", fontsize=13)

ax.set_ylim((0.5, 11))
ax.set_yticks([])

fig.tight_layout()
fig.savefig("a-nmr.png", dpi=600)
