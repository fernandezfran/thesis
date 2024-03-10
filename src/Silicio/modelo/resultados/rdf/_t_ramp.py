#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2024, Francisco Fernandez
# License: CC BY-SA 4.0
#   https://github.com/fernandezfran/thesis/blob/main/LICENSE
import matplotlib.pyplot as plt
import numpy as np

t_ramp = np.loadtxt("_t_ramp.dat")
x = list(range(0, 100 * len(t_ramp), 100))

plt.rcParams.update({"font.size": 12})

fig, ax = plt.subplots(figsize=(7, 5))

ax.text(0.02e6, 300, "calentamiento", rotation=77, color="tab:blue")
ax.plot(x[:1000], t_ramp[:1000])

ax.text(0.3e6, 1800, "termalización", color="tab:orange")
ax.plot(x[1000:8500], t_ramp[1000:8500])

ax.text(1e6, 3000, "enfriamiento", color="tab:green")
ax.plot(x[8500:], t_ramp[8500:])

ax.set_xlim((0.0, 1.45e6))
ax.set_xlabel(r"$t$ (ps)")

ax.set_ylim((0, 4600))
ax.set_yticks([0, 300, 1500, 3000])
ax.set_ylabel("T (K)")

fig.savefig("_t_ramp.png", dpi=600)
