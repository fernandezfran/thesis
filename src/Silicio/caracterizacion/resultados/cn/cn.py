#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2024, Francisco Fernandez
# License: CC BY-SA 4.0
#   https://github.com/fernandezfran/thesis/blob/main/LICENSE
import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams.update({"font.size": 16})

fig, ax = plt.subplots(ncols=2, figsize=(13, 5))

ls = "dashed"
interacciones = ["LiLi", "SiLi", "SiSi"]
colores = ["tab:green", "tab:orange", "tab:blue"]
markers = ["o", "^", "s"]
for e, c, m in zip(interacciones, colores, markers):
    dataset = pd.read_csv(
        f"datasets/cn/{e}.dat",
        delimiter="\t",
        comment="#",
        names=["x", "cn_mean", "cn_err"],
    )
    ax[0].errorbar(
        dataset.x,
        dataset.cn_mean,
        yerr=dataset.cn_err,
        marker=m,
        color=c,
        linestyle=ls,
        linewidth=1,
        capsize=2.5,
        elinewidth=1,
        label=f"{e}",
    )

    dataset = pd.read_csv(
        f"datasets/cn2/{e}.dat",
        delimiter="\t",
        comment="#",
        names=["x", "cn_mean", "cn_err"],
    )
    ax[1].errorbar(
        dataset.x,
        dataset.cn_mean,
        yerr=dataset.cn_err,
        marker=m,
        color=c,
        linestyle=ls,
        linewidth=1,
        capsize=2.5,
        elinewidth=1,
        label=f"{e}",
    )

ax[0].set_ylabel("CN")
for axis in ax:
    axis.set_xlabel(r"$x$ en Li$_x$Si")
    axis.secondary_xaxis(
        "top", functions=(lambda x: 4056.2 * x / 4.25, lambda x: 4056.2 * x / 4.25)
    ).set_xlabel(r"Capacidad (mAhg$^{-1}$)")
    axis.grid(axis="y", linestyle=":")
    axis.set_xlim((0, 4.25))

ax[0].legend()

ax[0].text(0.0, 1.15, "(a)", transform=ax[0].transAxes)
ax[1].text(0.92, 1.15, "(b)", transform=ax[1].transAxes)

fig.tight_layout()
fig.savefig("cn.png", dpi=600)
