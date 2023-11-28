#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2024, Francisco Fernandez
# License: CC BY-SA 4.0
#   https://github.com/fernandezfran/thesis/blob/main/LICENSE
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.8, 4, 500)

xinv6 = 1 / x ** 6
xinv12 = 1 / x ** 12
lj = 4 * (xinv12 - xinv6)

plt.rcParams.update({"font.size": 12})

plt.xticks([0, 1, 2, 3, 4])
plt.xlim((0, 4))
plt.ylim((-1.5, 3.5))
plt.xlabel(r"r/$\sigma$")
plt.ylabel(r"V$_{LJ}$/$\varepsilon$")

plt.axhline(y=0, color="k", linestyle="--", linewidth=1)
plt.plot(x, lj, linewidth=2)

plt.savefig("lj.png", dpi=600)
