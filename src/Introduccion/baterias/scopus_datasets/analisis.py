#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2024, Francisco Fernandez
# License: CC BY-SA 4.0
#   https://github.com/fernandezfran/thesis/blob/main/LICENSE
import pandas as pd

files = [
    "lithium_battery.csv",
    "lithium_battery_fast-charging.csv",
    "lithium_battery_Si-anodes.csv",
]

print("archivo: % promedio de incremento anual")
for file in files:
    dataset = pd.read_csv(file)
    dataset = dataset.sort_values(by="year", ascending=True)

    print(f"{file}: {dataset.npub.pct_change()[10:].mean():.2f}")
