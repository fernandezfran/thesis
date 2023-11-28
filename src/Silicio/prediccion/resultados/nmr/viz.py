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
si_centers = [(0, 2.5), (2.7, 2.5), (0, -2), (-4, 4)]

silicons = (
    [plt.Circle(si_centers[0], rsi, color="tab:blue", label="Si")]
    + [plt.Circle(center, rsi, color="tab:blue") for center in si_centers[1:]]
    + [
        plt.Circle(
            (center[0] + img[0], center[1] + img[1]),
            radius=rsi,
            color="tab:blue",
            alpha=0.5,
        )
        for center, img in it.product(si_centers, pbc)
    ]
)

rli = 0.2
li_centers = [
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
lithiums = (
    [plt.Circle((li_centers[0]), rli, color="tab:green", label="Li")]
    + [plt.Circle(center, rli, color="tab:green") for center in li_centers[1:]]
    + [
        plt.Circle(
            (center[0] + img[0], center[1] + img[1]),
            radius=rli,
            color="tab:green",
            alpha=0.5,
        )
        for center, img in it.product(li_centers, pbc)
    ]
)

rcuts = [
    plt.Circle(
        center, 3.4, color="tab:green", linestyle="dashed", linewidth=2, fill=False
    )
    for center in li_centers
]
fig, ax = plt.subplots()

ax.text(0.25, -0.25, "1")
ax.text(1.25, 4.25, "2")
ax.text(-2, -3.75, "3")

# box
ax.vlines([-5, 5], [-10, -10], [10, 10], linestyle="dashed", colors="gray")
ax.hlines([-5, 5], [-10, -10], [10, 10], linestyle="dashed", colors="gray")

ax.vlines([-5, 5], [-5, -5], [5, 5], colors="k")
ax.hlines([-5, 5], [-5, -5], [5, 5], colors="k")


for circ in silicons + lithiums + rcuts[:3]:
    ax.add_patch(circ)

# silicon bonds
ax.plot([0, 2.7], [2.5, 2.5], color="tab:blue")
# images
ax.plot([-10 + rsi, -7.3 - rsi], [2.5, 2.5], color="tab:blue", alpha=0.5)
ax.plot([rsi, 2.7 - rsi], [-7.5, -7.5], color="tab:blue", alpha=0.5)
ax.plot([-10 + rsi, -7.3 - rsi], [-7.5, -7.5], color="tab:blue", alpha=0.5)

ax.set_xlim((-10, 10))
ax.set_ylim((-10, 10))
ax.set_aspect("equal", adjustable="box")

ax.set_xticks([])
ax.set_yticks([])

ax.set_xlabel("x")
ax.set_ylabel("y")

ax.legend(ncol=2, bbox_to_anchor=(0.737, 1.11), edgecolor="1.0")

fig.savefig("viz.png", dpi=600)
plt.show()
