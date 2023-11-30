#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2024, Francisco Fernandez
# License: CC BY-SA 4.0
#   https://github.com/fernandezfran/thesis/blob/main/LICENSE
import matplotlib.pyplot as plt

years = [1992, 1995, 1996, 1998, 2000, 2001, 2002, 2005, 2008, 2012, 2015, 2023]
whkg = [81, 111, 122, 141, 160, 166, 171, 212, 227, 263, 301, 360]

plt.scatter(years, whkg, c="tab:blue")

plt.text(1992, 200, "Sony")
plt.arrow(1993, 195, -0.85, -100, fc="k", head_width=0.5, head_length=5)

plt.text(2019, 200, "WeLion")
plt.arrow(2021, 215, 1.85, 130, fc="k", head_width=0.5, head_length=5)

plt.xticks(range(1990, 2026, 5))
plt.xlabel("Año")
plt.ylabel("Densidad de energía (Wh/kg)")
plt.ylim((0, 400))

plt.tight_layout()
plt.savefig("whkg.png", dpi=600)
