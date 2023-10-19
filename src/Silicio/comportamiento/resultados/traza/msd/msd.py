#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    import matplotlib.pyplot as plt
    import numpy as np
    import pandas as pd
    import sklearn.linear_model

    plt.rcParams.update({'font.size': 12})

    structures = ("crystal", "amorphous")
    temps = np.array([800, 1000, 1200, 1400, 1500, 1600])

    colors = ["tab:blue", "tab:orange", "tab:green", "tab:red", "tab:purple", "tab:pink"]
    titles = ["c-Si", "a-Si"]

    fig, ax = plt.subplots(ncols=2, sharex=True, figsize=(12, 5))

    for k, s in enumerate(structures):
        for i, temp in enumerate(temps):
            df = pd.read_csv(f"data/{s}-{temp}.csv")
            t, msd = df["t"].to_numpy().reshape(-1, 1), df["msd"].to_numpy()

            reg = sklearn.linear_model.LinearRegression()
            reg.fit(t[400:t.size - 200, :], msd[400:msd.size - 200])
            pred = reg.predict(t)

            ax[k].scatter(t, msd, color=colors[i], marker=".", alpha=0.1)
            ax[k].plot(t, pred, color=colors[i], label=temp)

        ax[k].set_xlim((40, 80))
        ax[k].set_ylim((7, 1000))

        ax[k].set_xscale("log")
        ax[k].set_yscale("log")

        ax[k].set_xlabel("t [ps]")
        ax[k].set_ylabel(r"MSD [$\AA^2$]")

        ax[k].set_title(titles[k])

    ax[0].legend()

    fig.savefig("msd.png", dpi=600)

    plt.show()
