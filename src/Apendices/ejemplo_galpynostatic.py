#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2024, Francisco Fernandez
# License: CC BY-SA 4.0
#   https://github.com/fernandezfran/thesis/blob/main/LICENSE
import galpynostatic
import numpy as np

# datos del grafito
C_rates = np.array([0.1, 0.2, 1 / 3, 0.5, 1, 3, 5, 7, 10]).reshape(-1, 1)
soc = np.array([0.992, 0.982, 0.965, 0.935, 0.854, 0.540, 0.297, 0.195, 0.125])

# cargamos los datos del diagrama para la geometría esférica
dataset = galpynostatic.datasets.load_spherical()

# longitud de difusión característica en cm
d = 7.5e-4

# regresor galvanostático: modelo heurístico
greg = galpynostatic.model.GalvanostaticRegressor(dataset, d, 3)

# ajuste del modelo
greg.fit(C_rates, soc)

# obtención del coeficiente de difusión y la constante cinética
greg.dcoeff_
greg.k0_

# gráfico de datos predichos versus los experimentales
greg.plot.versus_data(C_rates, soc)
