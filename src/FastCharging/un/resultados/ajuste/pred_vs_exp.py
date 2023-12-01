#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2024, Francisco Fernandez
# License: CC BY-SA 4.0
#   https://github.com/fernandezfran/thesis/blob/main/LICENSE
from sklearn.metrics import r2_score

from shared import *

fig, ax = plt.subplots()

for sys, greg, X, y, m, c in zip(systems, models, X_data, y_data, markers, colors):
    y_pred = greg.predict(X)
    r2 = f"{sys}: {r2_score(y, y_pred):.3f}"

    ax.scatter(y, y_pred, marker=m, color=c, alpha=0.75, label=r2)

ax.plot([-0.1, 1.1], [-0.1, 1.1], ls="dashed", c="tab:gray", alpha=0.75)

ax.set_xlim((0.05, 1.05))
ax.set_xlabel(r"Valor experimental de SOC$_{max}$")

ax.set_ylim((0.05, 1.05))
ax.set_ylabel(r"Predicción de SOC$_{max}$")

ax.legend(title="R$^2$")

fig.tight_layout()
fig.savefig("pred_vs_exp.png", dpi=600)
