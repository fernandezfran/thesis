#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams.update({"font.size": 12})

fig, ax = plt.subplots()

for i, (experimento, m, l) in enumerate(
    zip(["litiada", "amorfa"], ["^", "v"], ["Si litiado", "Si amorfo"])
):
    df = pd.read_csv(f"datos/pdf-{experimento}.csv")
    ax.scatter(df.r, df.gofr, color="k", marker=m, label=l)

    for metodo, c, ls, l in zip(
        ["cristal", "DFTB"],
        ["tab:orange", "tab:blue"],
        ["dashed", "solid"],
        ["cristalinas", "DFTB"],
    ):
        df = pd.read_csv(f"datos/pdf-{experimento}-{metodo}.csv")

        l = None if i == 0 else l
        ax.plot(df.r, df.gofr, color=c, ls=ls, label=l)


ax.set_xlim((2.1, 5.5))

ax.set_xlabel(r"r ($\AA$)")
ax.set_ylabel(r"G(r) ($\AA^{-2}$)")

ax.legend()

fig.tight_layout()
fig.savefig("pdfs.png", dpi=600)
