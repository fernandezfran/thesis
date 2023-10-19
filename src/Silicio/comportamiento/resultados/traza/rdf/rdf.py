#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    import matplotlib.pyplot as plt
    import numpy as np
    import pandas as pd

    plt.rcParams.update({'font.size': 12})

    structures = ("crystal", "amorphous")
    temps = np.array([800, 1000, 1200, 1400, 1500, 1600])

    colors = ["tab:blue", "tab:orange", "tab:green", "tab:red", "tab:purple", "tab:pink"]
    titles = ["c-Si", "a-Si"]

    fig, ax = plt.subplots(ncols=2, sharex=True, figsize=(12, 5))

    for k, s in enumerate(structures):
        for i, temp in enumerate(temps):
            df = pd.read_csv(f"data/{s}-{temp}.csv")

            ax[k].plot(df["r"], df["rdf"], color=colors[i], label=temp)

        ax[k].set_xlim((1.5, 5))
        ax[k].set_ylim((0, 5.5))

        ax[k].set_xlabel(r"r [$\AA$]")
        ax[k].set_ylabel("RDF")

        ax[k].set_title(titles[k])

    ax[1].legend()

    fig.savefig("rdf.png", dpi=600)

    plt.show()
