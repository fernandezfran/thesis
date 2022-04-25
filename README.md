# Simulaciones computacionales para el desarrollo de electrodos de baterias de ion-litio de próxima generación

Tesis doctoral realizada en el Laboratorio de Energías Sustentables
([LaES](http://www.laesunc.com/laes/)), que es parte de la Facultad de Matemática, 
Astronomía, Física y Computación ([FAMAF](https://www.famaf.unc.edu.ar/)), 
la Facultad de Ciencias Químicas ([FCQ](http://www.fcq.unc.edu.ar/))
y la Facultad de Ciencias Exactas, Física y Naturales ([FCEFyN](https://fcefyn.unc.edu.ar/))
de la Universidad Nacional de Córdoba ([UNC](https://www.unc.edu.ar/)). 

Director: Daniel Eugenio Barraco Díaz

Codirector: Ezequiel Pedro Marcos Leiva


----------------------------------------------------------------------------------

## Requisitos

Para la obtención del título del Doctor en Física se necesita cumplir con distintos
requisitos, algunos de ellos:

### Cursos de posgrado realizados

+ [Diseño de software para cómputo científico](https://github.com/leliel12/diseno_sci_sfw), 
como proyecto final escribí [sierras](https://github.com/fernandezfran/sierras), 
una librería de Python.

+ [Computación paralela](https://cs.famaf.unc.edu.ar/~nicolasw/Docencia/CP/2020/index.html), 
para el cual paralelicé [tiny_md](https://github.com/fernandezfran/tiny_md), 
un código de dinámica molecular que escribí para la materia.        

+ [Física computacional](https://github.com/fernandezfran/fiscomp).

+ Simulaciones computacionales en sistemas de materia condensada.

+ Electroquímica.

+ Resonancia magnética nuclear.

### Seminarios dictados

1. "Potenciales interatómicos de aprendizaje automático y su aplicación a 
baterías de litio". 22 de Abr, 2022. _Aula Magna, FAMAF._


----------------------------------------------------------------------------------

## Publicaciones científicas

1. <ins>F. Fernandez</ins>, A. Paz, M. Otero, D. Barraco, E. Leiva.
"Characterization of amorphous Li<sub>x</sub>Si structures from ReaxFF via
accelerated exploration of local minima". _Physical Chemistry Chemical Physics_
(2021). https://doi.org/10.1039/D1CP02216D


## Presentaciones en congresos

+ <ins>F. Fernandez</ins>, S. A. Paz, M. Otero, D. E. Barraco Dı́az, E. P. M. Leiva.
"Comportamiento electroquímico y estructural de ánodos de Silicio a partir de
simulaciones computacionales". _1 er Encuentro Nacional sobre Litio_
1--3 de Dic, 2021. _Buenos Aires, Argentina._

+ <ins>F. Fernandez</ins>, S. A. Paz, M. Otero, D. E. Barraco Dı́az, E. P. M. Leiva.
"Amorphous Li-Si structures found via a novel simulation method using a reactive 
force field". _8 th International Workshop on Lithium, Industrial Minerals and 
Energy (IWLiME)_ 8--10 de Nov, 2021. _Cochabamba, Bolivia._

+ E. P. M. Leiva, M. Gavilán-Arriazu, <ins>F. Fernandez</ins>, D. E. Barraco Díaz.
"Kinectic Modeling on Lithium-ion Instertion in Prototypical Systems". _72 nd 
Annual Meeting of the International Society of Electrochemistry_ 29 de Ago--3 de
Sep, 2021. _Jeju Island, Korea/Online (Hybrid)._

+ E. P. M. Leiva, <ins>F. Fernandez</ins>. "Un viaje por el Nanomundo de las 
baterias de Li". _XXII Congreso Argentino de Fisicoquímica y Química Inorganica_
19--29 de Abr, 2021. _La Plata, Argentina._

+ <ins>F. Fernandez</ins>, M. Otero, S. A. Paz, D. E. Barraco Dı́az, E. P. M. Leiva.
"First steps towards reproducing chemical shifts spectra of c-LiSi alloys using 
a semi-empirical force field". _7 th International Workshop on Lithium, 
Industrial Minerals and Energy (IWLiME)_ 9--11 de Nov, 2020. _Antofagasta, Chile._


----------------------------------------------------------------------------------

## Instrucciones para generar la tesis

Para compilar la tesis en Linux a través del `Makefile` es necario tener instalado
`LaTeX`, `pdflatex` y `latexmk`.
    
```bash
make
xdg-open tesis.pdf
make clean
```

> En Linux, `xdg-open` abre el lector de pdf predeterminado. 
