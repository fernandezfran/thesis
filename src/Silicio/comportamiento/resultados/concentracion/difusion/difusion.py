#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    import matplotlib.pyplot as plt
    import numpy as np
    import pandas as pd

    plt.rcParams.update({'font.size': 12})

    fig, ax = plt.subplots()

    df = pd.read_csv("../data.csv")

    ax.scatter(df["x"], df["D"])

    ax.set_yscale("log")

    ax.set_xlabel(r"x en Li$_x$Si")

    ax.set_ylabel(r"D (cm$^2$/s)")
    ax.secondary_xaxis(
        "top", functions=(lambda x: 4056.2 * x / 4.25, lambda x: 4056.2 * x / 4.25)
    ).set_xlabel(r"Capacidad (mAhg$^{-1}$)")

    fig.tight_layout()
    fig.savefig("comportamiento-D.png", dpi=600)

    plt.show()
