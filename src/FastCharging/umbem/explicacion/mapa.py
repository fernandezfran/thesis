#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2024, Francisco Fernandez
# License: CC BY-SA 4.0
#   https://github.com/fernandezfran/thesis/blob/main/LICENSE
import galpynostatic
import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams.update({"font.size": 14})

spherical = pd.read_csv("../datasets/simulated_spherical_map_200mV.csv")

greg = galpynostatic.model.GalvanostaticRegressor(spherical, 1, 1)
greg._map = galpynostatic.base.MapSpline(spherical)
greg.plot.render_map(clb_label="UMBEM")

plt.tight_layout()
plt.savefig("mapa.png", dpi=600)
