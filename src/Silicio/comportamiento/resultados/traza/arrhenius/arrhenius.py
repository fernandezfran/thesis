#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def invert(x):
    # 1/x with special treatment of x == 0
    x = np.array(x).astype(float)
    near_zero = np.isclose(x, 0)
    x[near_zero] = np.inf
    x[~near_zero] = 1 / x[~near_zero]
    return x


if __name__ == "__main__":
    import matplotlib.pyplot as plt
    import numpy as np
    import pandas as pd
    import sierras

    structures = ("crystal", "amorphous")

    activation_energies = np.zeros(len(structures))
    room_dcoeffs = np.zeros(len(structures))

    colors = ["tab:blue", "tab:orange"]
    markers = ["s", "o"]
    labels = ["c-Si", "a-Si"]

    fig, ax = plt.subplots()

    for i, s in enumerate(structures):
        df = pd.read_csv(f"data/{s}.csv")
        temps, dcoeffs, dcoeffs_err = (
            df["temps"].to_numpy().reshape(-1, 1),
            df["dcoeffs"].to_numpy(),
            df["dcoeffs_err"].to_numpy(),
        )

        k_boltzmann = 8.617333262e-5  # eV / K
        areg = sierras.ArrheniusRegressor(k_boltzmann)

        areg.fit(temps, dcoeffs, sample_weight=dcoeffs_err)

        activation_energies[i] = areg.activation_energy_
        room_dcoeffs[i] = areg.extrapolated_process_

        print(f"{s},{activation_energies[i]:.2f},{room_dcoeffs[i]:.3e}")

        areg.plot.arrhenius(
            temps,
            dcoeffs,
            ax=ax,
            data_kws={"color": colors[i], "marker": markers[i], "label": ""},
            pred_kws={"label": labels[i]},
        )

    ax.ticklabel_format(axis="x", style="sci", scilimits=(0, 0))

    ax.set_xlabel("1 / T (1 / K)")
    secax = ax.secondary_xaxis("top", functions=(invert, invert))
    secax.set_xlabel("T (K)")

    ax.set_ylabel(r"log (D / (cm$^2$/s))")

    ax.legend()

    fig.savefig("arrhenius.png", dpi=600)
    plt.show()
