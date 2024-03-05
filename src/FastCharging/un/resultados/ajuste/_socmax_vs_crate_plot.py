#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2024, Francisco Fernandez
# License: CC BY-SA 4.0
#   https://github.com/fernandezfran/thesis/blob/main/LICENSE
from shared import *

index = 3
X, y = X_data[index], y_data[index]

plt.scatter(X, y, marker="s")

plt.xscale("log")
plt.xlabel("C-rate")
plt.ylabel(r"$SOC_{\max}$")

plt.savefig("_socmax_vs_crate_plot.png", dpi=600)
plt.show()
