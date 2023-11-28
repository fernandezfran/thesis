#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2024, Francisco Fernandez
# License: CC BY-SA 4.0
#   https://github.com/fernandezfran/thesis/blob/main/LICENSE
import galpynostatic
import matplotlib.pyplot as plt

plt.rcParams.update({'font.size': 14})

greg = galpynostatic.model.GalvanostaticRegressor()
greg.fit([[4.0], [5.0]], [0.8, 0.9])

fig, ax = plt.subplots(figsize=(6, 5))
ax = greg.plot.render_map(ax=ax, clb_label="valor máximo del SOC")

ax.plot([-4, 1.75], [0, 0], ls="--", color="tab:gray")
ax.text(-3.8, 0.2, "(b)", color="tab:gray")

ax.plot([-4, 1.75], [-2, -2], ls="--", color="tab:gray")
ax.text(-3.8, -1.8, "(c)", color="tab:gray")

ax.scatter(-1, -1, marker="^", color="tab:blue")
ax.text(-1.1, -0.9, "A", color="tab:blue")

ax.scatter(1.5, 1, marker="v", color="tab:red")
ax.text(1.4, 0.67, "B", color="tab:red")

ax.text(-4., 2.25, "(a)")

plt.savefig("diagnosis-map.png", dpi=600)
