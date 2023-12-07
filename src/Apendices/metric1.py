# velocidad de carga galvanostática de 15 minutos
C_rate = np.array([[4.0]])

# información del material
info = {
    "d": 0.001, # [cm]
    "dcoeff_": 1.07e-12, # [cm^2/s]
    "k0_": 1.0e-7, # [cm/s]
}

# UMBEM con full_output True
output = galpynostatic.metric.umbem(
    info, full_output=True
)

# valor de UMBEM
output.value

# True si es mayor a 0.8 y False si no
output.criteria

# grafica el punto en el mapa universal construído con
# simulaciones
output.greg.plot.in_map(C_rate)
