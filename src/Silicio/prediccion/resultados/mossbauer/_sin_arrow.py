#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2024, Francisco Fernandez
# License: CC BY-SA 4.0
#   https://github.com/fernandezfran/thesis/blob/main/LICENSE
import numpy as np
import matplotlib.pyplot as plt

n = 5

fig, ax = plt.subplots()

ax.text(n * np.pi / 2, 1.1, r"$\gamma$", fontsize=50, fontweight="bold")

x = np.linspace(0, n * np.pi, 1000)
ax.plot(x, np.sin(x), color="k", lw=10, ls="--")

ax.arrow(
    n * np.pi,
    0,
    n / 5,
    0,
    lw=10,
    head_width=0.1,
    head_length=0.4,
    fc="k",
    ec="k",
)

ax.axis("off")

fig.savefig("_sin_arrow.png")
plt.show()
