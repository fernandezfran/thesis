#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Densidad de energía volumétrica vs gravimétrica."""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

nordgray = "#2E3440"
nordred = "#BF616A"
nordorange = "#D08770"
nordyellow = "#EBCB8B"
nordpink = "#B48EAD"
nordgreen = "#A3BE8C"
nordblue = "#5E81AC"


plt.rcParams.update({"font.size": 12})
fig, ax = plt.subplots()

ax.set_xlim((0, 700))
ax.set_ylim((0, 1100))

ax.set_xlabel(r"Densidad de energía gravimétrica [Wh/kg]")
ax.set_ylabel(r"Densidad de energía volumétrica [Wh/L]")

ax.text(475, 17.5, "Más livianas", fontsize=14)
ax.text(10, 750, "Más chicas", rotation="vertical", fontsize=14)

ax.arrow(40, 750, 0, 300, width=2, length_includes_head=True, head_length=15, head_width=5, color=nordgray)
ax.arrow(475, 75, 180, 0, width=2, length_includes_head=True, head_length=10, head_width=10, color=nordgray)

ax.text(5, 20, "Plomo-ácido")
lead_acid = mpatches.Ellipse((27, 67), 20, 38, color=nordgray, alpha=1)
ax.add_patch(lead_acid)

ax.text(39, 132, "NiCd")
nicd = mpatches.Ellipse(
    (46, 132),
    140,
    35,
    angle=85,
    color=nordred,
    alpha=1,
)
ax.add_patch(nicd)

ax.text(78, 183, "NiMH")
nimh = mpatches.Ellipse((87, 183), 20, 200, angle=-5, color=nordorange, alpha=1)
ax.add_patch(nimh)

ax.text(90, 440, "Estado del arte LIB")
lib_now = mpatches.Ellipse((180, 440), 100, 550, angle=-12, color=nordgreen, alpha=1)
ax.add_patch(lib_now)

ax.text(400, 930, "Litio metálico")
lib_li = mpatches.Ellipse((475, 930), 80, 200, angle=-30, color=nordyellow, alpha=1)
ax.add_patch(lib_li)

ax.text(460, 320, "Litio-aire")
lia = mpatches.Ellipse((550, 550), 150, 500, angle=-30, color=nordblue, alpha=1)
ax.add_patch(lia)

ax.text(360, 550, "Litio-azufre")
lis = mpatches.Ellipse((480, 510), 100, 380, angle=-25, color=nordpink, alpha=1)
ax.add_patch(lis)

fig.savefig("densidad_de_energia.png", dpi=600)
