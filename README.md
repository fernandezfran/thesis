# Simulaciones computacionales para el desarrollo de electrodos de baterias de ion-litio de próxima generación

Tesis doctoral realizada en el Laboratorio de Energías Sustentables
([LaES](http://www.laesunc.com/laes/)), que es parte de la Facultad de Matemática, 
Astronomía, Física y Computación ([FAMAF](https://www.famaf.unc.edu.ar/)), 
la Facultad de Ciencias Químicas ([FCQ](http://www.fcq.unc.edu.ar/))
y la Facultad de Ciencias Exactas, Física y Naturales ([FCEFyN](https://fcefyn.unc.edu.ar/))
de la Universidad Nacional de Córdoba ([UNC](https://www.unc.edu.ar/)). 

Director: Daniel Eugenio Barraco Díaz

Codirector: Ezequiel Pedro Marcos Leiva


## Publicaciones

1. <ins>F. Fernandez</ins>, A. Paz, M. Otero, D. Barraco, E. Leiva.
   "Characterization of amorphous Li<sub>x</sub>Si structures from ReaxFF via
   accelerated exploration of local minima". _Physical Chemistry Chemical Physics_
   (2021). https://doi.org/10.1039/D1CP02216D


## Instrucciones para generar la tesis

Para compilar la tesis en Linux a través del `Makefile` es necario tener instalado
`LaTeX`, `pdflatex` y `latexmk`.
    
```bash
make
xdg-open tesis.pdf
make clean
```

> En Linux, `xdg-open` abre el lector de pdf predeterminado. 
