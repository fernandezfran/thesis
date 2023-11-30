#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2024, Francisco Fernandez
# License: CC BY-SA 4.0
#   https://github.com/fernandezfran/thesis/blob/main/LICENSE
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({"font.size": 12})

years = np.arange(2014, 2024)
sales = np.array([320, 543, 791, 1262, 2082, 2276, 3245, 6768, 10532, 14000])

print(np.diff(sales) / sales[1:])

fig, ax = plt.subplots()

ax.bar(years, 1000 * sales, width=0.6)

ax.set_xticks(years)
ax.set_xlabel("Año")

ax.set_ylabel("Ventas anuales de vehículos eléctricos")

fig.tight_layout()
fig.savefig("ev-volumes.png", dpi=600)
