#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2024, Francisco Fernandez
# License: CC BY-SA 4.0
#   https://github.com/fernandezfran/thesis/blob/main/LICENSE
import itertools as it

import matplotlib.pyplot as plt

plt.rcParams.update({"font.size": 12})

pbc = list(it.product((-10, 0, 10), repeat=2))

rsi = 0.25
si_centros = [(0.35, 2.8), (3.05, 2.8), (-0.7, -2), (-3.8, 4.4)]

silicons = (
    [plt.Circle(si_centros[0], rsi, color="tab:blue", label="Si")]
    + [plt.Circle(center, rsi, color="tab:blue") for center in si_centros[1:]]
    + [
        plt.Circle(
            (center[0] + img[0], center[1] + img[1]),
            radius=rsi,
            color="tab:blue",
            alpha=0.5,
        )
        for center, img in it.product(si_centros, pbc)
    ]
)

rli = 0.2
li_centros = [
    (0, 0),
    (1.0, 4.5),
    (-2.25, -3.5),
    (-3.2, 1.4),
    (3.8, -1.3),
    (4.4, 3.4),
    (-1.6, 4.0),
    (-3.1, -0.9),
    (1.7, -3),
    (4.6, -3.5),
    (2.8, 0.9),
]
litios = (
    [plt.Circle((li_centros[0]), rli, color="tab:green", label="Li")]
    + [plt.Circle(center, rli, color="tab:green") for center in li_centros[1:]]
    + [
        plt.Circle(
            (center[0] + img[0], center[1] + img[1]),
            radius=rli,
            color="tab:green",
            alpha=0.5,
        )
        for center, img in it.product(li_centros, pbc)
    ]
)

rcuts = [
    plt.Circle(
        center, 3.4, color="tab:green", linestyle="dashed", linewidth=2, fill=False
    )
    for center in li_centros
]

fig, ax = plt.subplots()

ax.text(0.25, -0.25, "1")
ax.text(1.25, 4.25, "2")
ax.text(-2, -3.75, "3")

ax.vlines([-5, 5], [-10, -10], [10, 10], linestyle="dashed", colors="gray")
ax.hlines([-5, 5], [-10, -10], [10, 10], linestyle="dashed", colors="gray")

ax.vlines([-5, 5], [-5, -5], [5, 5], colors="k")
ax.hlines([-5, 5], [-5, -5], [5, 5], colors="k")


for circ in silicons + litios + rcuts[:3]:
    ax.add_patch(circ)

ax.plot([0.35, 3.0], [2.8, 2.8], color="tab:blue")

ax.plot([-9.65 + rsi, -7.0 - rsi], [2.8, 2.8], color="tab:blue", alpha=0.5)
ax.plot([0.35 + rsi, 3.0 - rsi], [-7.2, -7.2], color="tab:blue", alpha=0.5)
ax.plot([-9.65 + rsi, -7.0 - rsi], [-7.2, -7.2], color="tab:blue", alpha=0.5)

ax.set_xlim((-10, 10))
ax.set_ylim((-10, 10))
ax.set_aspect("equal", adjustable="box")

ax.set_xticks([])
ax.set_yticks([])

ax.set_xlabel("x")
ax.set_ylabel("y")

ax.legend(ncol=2, bbox_to_anchor=(0.737, 1.11), edgecolor="1.0")

fig.tight_layout()
fig.savefig("viz.png", dpi=600)
