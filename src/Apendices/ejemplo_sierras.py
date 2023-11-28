#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2024, Francisco Fernandez
# License: CC BY-SA 4.0
#   https://github.com/fernandezfran/thesis/blob/main/LICENSE
from sierras import ArrheniusRegressor

# ajuste de la ecuación de arrhenius, donde dcoeff son los coeficientes de
# difusión para cada temperatura en temperaturas
arrhenius = ArrheniusRegressor()
arrhenius.fit(temperaturas, dcoeff)

# obtención de la energía de activación
arrhenius.activation_energy_

# extrapolación a temperatura ambiente (300K) del coeficiente de difusión
arrhenius.predict([[300.0]])

# gráfico ln(D) versus 1/T
arrhenius.plot()
