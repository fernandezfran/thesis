import macchiato.chemical_shift
import MDAnalysis as mda
import pandas as pd

# datos experimentales del corrimiento químico de
# c-Li13Si4
experimental_nmr = pd.read_csv("Li13Si4.csv")
ppm = experimental_nmr["ppm"].to_numpy().reshape(-1, 1)
intensity = experimental_nmr["intensity"]

# posiciones atómicas de Li13Si4 del materials project
u = mda.Universe("Li13Si4.xyz")

# obtención de los centros de los picos de cada átomo
# utilizando el modelo de vecinos más cercanos
csc = macchiato.chemical_shift.ChemicalShiftCenters(u)
csc.fit(ppm)

# dados los centros, ajuste del ancho y la altura de los
# picos para coincidir con la precisión experimental
csw = macchiato.chemical_shift.ChemicalShiftWidth(csc)
csw.fit(ppm, intensity)

# gráfico del espectro predicho versus el experimental
plotter = macchiato.chemical_shift.ChemicalShiftSpectra(
    csc, csw
)
plotter.plot.versus_data(ppm, intensity)
