#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# https://stackoverflow.com/questions/25668828/how-to-create-colour-gradient-in-python

"""Ejemplo para generar gradiente de colores entre dos extremos nord."""

import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np


def color_fader(c1, c2, mix):
    c1 = np.array(colors.to_rgb(c1))
    c2 = np.array(colors.to_rgb(c2))
    return colors.to_hex((1 - mix) * c1 + mix * c2)


nordblue = "#5E81AC"
nordgreen = "#A3BE8C"
n = 9

fig, ax = plt.subplots()
for i in range(n + 1):
    ax.axvline(i, color=color_fader(nordblue, nordgreen, i / n))
plt.show()