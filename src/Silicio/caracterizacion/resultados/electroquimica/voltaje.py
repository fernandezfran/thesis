#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Voltaje vs x."""

import matplotlib.pyplot as plt
import numpy as np

xfe, fe, dfe = np.loadtxt("data/voltaje/fe.dat", unpack=True)
x, fes, v = np.loadtxt("data/voltaje/fe-spline.dat", unpack=True)
xdft, vdft = np.loadtxt("data/voltaje/v-chev.dat", delimiter=",", unpack=True)
xexp1, vexp1 = np.loadtxt("data/voltaje/v1-exp.dat", delimiter=",", unpack=True)
xexp2, vexp2 = np.loadtxt("data/voltaje/v2-exp.dat", delimiter=",", unpack=True)

plt.rcParams.update({"font.size": 12})
fig, ax = plt.subplots()

ax.set_xlabel(r"$x$ en Li$_x$Si")
ax.secondary_xaxis(
    "top", functions=(lambda x: 4056.2 * x / 4.25, lambda x: 4056.2 * x / 4.25)
).set_xlabel(r"Capacidad (mAhg$^{-1}$)")
ax.set_ylabel(r"Voltaje (V vs Li/Li$^+$)")

ax.set_ylim((-0.01, 0.8))
ax.set_xlim((0, 4.25))

ax.plot(xexp1, vexp1, color="tab:blue", label="a-Si")
ax.plot(xexp2, vexp2, color="tab:blue")
ax.plot(xdft, vdft, color="k", label="DFT spline")
ax.plot(x, v, color="tab:orange", label="ReaxFF spline")

ax.legend(loc=3)

####################        formation energy inset         #######################
fontsize = 8

# left, bottom, width, height = [0.61, 0.527, 0.35, 0.35]  # font.size default
left, bottom, width, height = [0.55, 0.529, 0.35, 0.35]  # font.size 12
ax2 = fig.add_axes([left, bottom, width, height])

ax2.tick_params(axis="both", which="major", labelsize=fontsize)

ax2.set_ylim((-0.745, 0.575))
ax2.set_xlim((0, 4.25))

ax2.set_xlabel(r"$x$ en Li$_x$Si", fontsize=fontsize)
ax2.set_ylabel("Energía de formación [eV]", fontsize=fontsize)

ax2.scatter(xfe, fe, color="tab:orange", marker="s", s=15, label="ReaxFF")
ax2.plot(x, fes, color="tab:orange", label="spline")

ax2.legend(prop={"size": fontsize})
##################################################################################

# fig.tight_layout()  # font.size default

fig.savefig("voltaje.png", dpi=600)
plt.show()
