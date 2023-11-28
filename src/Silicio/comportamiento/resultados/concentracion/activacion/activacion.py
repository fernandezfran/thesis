#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2024, Francisco Fernandez
# License: CC BY-SA 4.0
#   https://github.com/fernandezfran/thesis/blob/main/LICENSE

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

plt.rcParams.update({'font.size': 12})

fig, ax = plt.subplots()

df = pd.read_csv("../data.csv")

ax.scatter(df["x"], df["E"])

ax.set_xlabel(r"x en Li$_x$Si")

ax.set_ylabel(r"E$_a$ (eV)")
ax.secondary_xaxis(
    "top", functions=(lambda x: 4056.2 * x / 4.25, lambda x: 4056.2 * x / 4.25)
).set_xlabel(r"Capacidad (mAhg$^{-1}$)")

fig.tight_layout()
fig.savefig("activacion.png", dpi=600)

plt.show()
