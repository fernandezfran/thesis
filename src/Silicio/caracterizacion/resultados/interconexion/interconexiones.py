#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2024, Francisco Fernandez
# License: CC BY-SA 4.0
#   https://github.com/fernandezfran/thesis/blob/main/LICENSE

"""Todos los graficos de interconexiones."""

import matplotlib.pyplot as plt
import numpy as np

concentraciones = np.array([[0.21, 0.62, 1.25], [1.71, 2.17, 2.71], [3.25, 3.75, 4.2]])
labels = ["0 átomos", "1 átomo", "2 átomo", "3 átomos", "4 átomos", "+5 átomos"]

plt.rcParams.update({"font.size": 10})
fig, axes = plt.subplots(3, 3, sharex=True, sharey=True)

fig.text(0.5, 0.005, r"r [$\AA$]", ha="center")
fig.text(0.005, 0.5, "RDF Si-Li", va="center", rotation="vertical")

for conc, axis in zip(concentraciones, axes):

     for x, ax in zip(conc, axis):
        ax.grid(axis="y", linestyle=":")

        ax.set_xlim((4, 8))
        ax.set_ylim((0.0, 1.75))

        ges = np.loadtxt(f"data/rdf/{x}.dat", unpack=True)

        for g, l in zip(ges[1:], labels):
            ax.plot(ges[0], g, label=l)
        ax.plot(ges[0], ges[1:].sum(axis=0), color="k", label="total")

        ax.text(6, 1.55, f"x = {x}")

        if x == 1.25:
            ax.legend(bbox_to_anchor=(1.04, 1), loc="upper left", prop={"size": 8})

fig.subplots_adjust(wspace=0.1, hspace=0.1)
fig.tight_layout()

fig.savefig("interconexiones.png", dpi=600)
