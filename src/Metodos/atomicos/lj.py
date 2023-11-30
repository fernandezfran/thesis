#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2024, Francisco Fernandez
# License: CC BY-SA 4.0
#   https://github.com/fernandezfran/thesis/blob/main/LICENSE
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({"font.size": 12})

dist = np.linspace(0.8, 4, 500)
epot = 4 * (1 / np.power(dist, 12) - 1 / np.power(dist, 6))

plt.plot(dist, epot, linewidth=2)
plt.axhline(y=0, color="k", linestyle="--", linewidth=1)

plt.xticks(range(5))
plt.xlim((0, 4))
plt.xlabel(r"r/$\sigma$")

plt.ylim((-1.5, 3.5))
plt.ylabel(r"V$_{LJ}$/$\varepsilon$")

plt.tight_layout()
plt.savefig("lj.png", dpi=600)
