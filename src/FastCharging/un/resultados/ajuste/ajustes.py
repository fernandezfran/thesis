#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2024, Francisco Fernandez
# License: CC BY-SA 4.0
#   https://github.com/fernandezfran/thesis/blob/main/LICENSE
from shared import *

fig, ax = plt.subplots(nrows=3, ncols=2, sharey=True, figsize=(7, 7))
ax = ax.ravel()

data_kws = {"linestyle": "", "label": "datos experimentales"}
pred_kws = {"label": "modelo"}
for i, (sys, greg, X, y, let) in enumerate(
    zip(systems, models, X_data, y_data, abcdef)
):
    greg.plot.versus_data(X, y, ax=ax[i], data_kws=data_kws, pred_kws=pred_kws)

    ax[i].set_ylabel("")
    ax[i].set_xlabel("")

    if i == 0:
        ax[i].legend(ncol=2, loc="upper right", bbox_to_anchor=(1.9, 1.3))
    if sys in ("LMO", "LNMO"):
        ax[i].set_xlabel("C-rates")
    if sys in ("NG", "LFP", "LMO"):
        ax[i].set_ylabel(r"SOC$_{max}$")

    ax[i].text(0.9, 0.9, f"({let})", transform=ax[i].transAxes)
    ax[i].text(0.05, 0.05, sys, transform=ax[i].transAxes)

fig.savefig("ajustes.png", dpi=600)
