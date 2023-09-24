#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

plt.rcParams.update({"font.size": 12})

fig, ax = plt.subplots()

aleaciones = ("c-Si", "a-Si", r"c-Li15Si4", r"a-Li15Si4")

for aleacion in aleaciones:
    df = pd.read_csv(f"datos/gofr-{aleacion}.csv")
    ax.plot(df.r, df.gofr, label=aleacion)

ax.set_xlim((2, 5.5))
ax.set_ylim((-4.9, 18))
ax.set_xlabel(r"r [$\AA$]")
ax.set_ylabel(r"G(r) [$\AA^{-2}$]")

ax.legend()

fig.tight_layout()
plt.savefig("gofrs.png", dpi=600)
