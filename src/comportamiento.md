# Comportamiento dinámico del litio en ánodos de Silicio

Comentar los problemas que surgen a la hora de calcular la difusión, el protocolo
que suele seguirse (maginn2019) y porqué se usa el Nosé-Hoover (basconi2013) en
vez de otros de rescaleo o estocásticos.

## Método del trazador

Difusión de un átomo de litio en una estructura de silicio (ReaxFF). 

Esto daba un valor de coeficiente de difusión bastante razonable (daba distinto 
si se consideraban distintas cantidades de átomos de silicio, la Li1Si64 es la que
da un valor justo en el medio de entre Li1Si216 y Li1Si512), la energía de 
activación extrapolada y la calculada sobre distintos nebs.

## Comportamiento del coeficiente de difusión en función de la concentración

Presentar estos resultados acá justificarían de alguna forma el cambio del ReaxFF 
a DFTB (mencionar los valores que se obtienen en otras simulaciones y en 
experimentos).

### ReaxFF

### DFTB
