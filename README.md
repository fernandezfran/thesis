# Computational modeling for the development of next-generation lithium-ion battery electrodes

> PhD thesis done at [FAMAF (Universidad Nacional de Córdoba)](https://www.famaf.unc.edu.ar/), working in the [LAES](http://www.laesunc.com/laes/) computational area.

[![License](https://img.shields.io/badge/License-CC%20BY%20SA%204.0-08fc04)](https://creativecommons.org/licenses/by-sa/4.0/)

**Advisors**: [Dr. Daniel Barraco](https://scholar.google.com/citations?user=DzOhPJMAAAAJ&hl=en) (FAMAF, Universidad Nacional de Córdoba) & [Dr. Ezequiel Leiva](https://scholar.google.com/citations?user=Hi9f4aUAAAAJ&hl=en) (FCQ, Universidad Nacional de Córdoba).

**Thesis committee**: [Dr. Roberto M. Torresi](https://scholar.google.com/citations?user=1EOqiw0AAAAJ&hl=en&oi=ao) (IQ, Universidade de São Paulo), [Dr. Alejandro A. Franco](https://scholar.google.com/citations?user=tzx61H8AAAAJ&hl=en&oi=ao) (LRCS, Université de Picardie Jules Verne), [Dr. Fabián Vaca Chávez](https://scholar.google.com/citations?user=XZEcNGQAAAAJ&hl=en&oi=ao) (FAMAF, Universidad Nacional de Córdoba), [Dra. Mariela G. Ortiz](https://scholar.google.com/citations?user=YlOo-_4AAAAJ&hl=en&oi=ao) (INIFTA, Universidad Nacional de La Plata) & [Dr. Andrés Ruderman](https://www.conicet.gov.ar/new_scp/detalle.php?id=43175&datos_academicos=yes) (FAMAF, Universidad Nacional de Córdoba).

**Abstract**: TODO


## Instructions to compile the thesis

To install all the requirements needed for the compilation of the thesis in 
a minimal installation (i.e. not the full `texlive` installation), run in a 
Linux terminal the following commands:
```
sudo apt update
sudo apt upgrade
sudo apt install -y $(cat requirements_TeX.txt)
```
Then, the thesis can be compiled using the Makefile:
```
cd src/
make
xdg-open thesis.pdf
```

To run the Python scripts to generate the figures of the thesis, the required 
libraries must be installed as follows:
```
pip install -r requirements_Python.txt
```

For the inspection of the structures VMD needs to be installed, Tcl 
configuration scripts are provided and can be run as
```
vmd -e config.tcl <input_structure>
```


## PhD requirements fulfilled

### Dissertation

Presented to the Faculty of Mathematics, Astronomy, Physics and Computer Science 
of the NATIONAL UNIVERSITY OF CÓRDOBA on March dd, 2024.


### Postgraduate courses

+ **Machine Learning School for Materials @ Ilum**, CNPEM. 20 hrs, Sep 5--7, 2022.

+ **Machine learning for scarse data**, ECI, DC, UBA. 15 hrs, Jul 26--30, 2021.

+ **Software design for scientific computing**, FAMAF, UNC. 60 hrs, 2021. 
[link](https://github.com/leliel12/diseno_sci_sfw).

+ **Python programming**, ECyT, UNSAM. 96 hrs, 2021.
[link](https://github.com/python-unsam/Programacion_en_Python_UNSAM).

+ **Parallel computing**, FAMAF, UNC. 120 hrs, 2020. 
[link](https://cs.famaf.unc.edu.ar/~nicolasw/Docencia/CP/2020/index.html).

+ **Computational physics**, FAMAF, UNC, 120 hrs, 2020.
[link](https://github.com/fernandezfran/fiscomp).

+ **Nuclear magnetic resonance**, FAMAF, UNC. 25 hrs, 2020.

+ **Computer simulations in condensed matter systems**, FCQ, UNC. 40 hrs, 2019.

+ **Electrochemistry**, FCQ, UNC. 80 hrs, 2019.

### Seminars talks

+ **Fast-charging lithium batteries: from designing materials to optimizing 
charging protocols**. Sep 14, 2023. _Aula Magna, FAMAF._

+ **Machine learning interatomic potentials and their application to lithium 
batteries**. Apr 22, 2022. _Aula Magna, FAMAF._ 

## Research activity

### Scientific articles

+ **UMBEM: A Universal Metric for Benchmarking fast-charging Electrode Materials**.
<ins>F. Fernandez</ins> _et al_. _Manuscript in preparation_, 2023.

+ **Towards a fast-charging of LIBs electrode materials: a heuristic model based 
on galvanostatic simulations**. <ins>F. Fernandez</ins>, E. M. Gavilán-Arriazu, 
D. E. Barraco, A. Visintín, Y. Ein-Eli, E. P. M. Leiva. 
[_Electrochimica Acta_](https://authors.elsevier.com/c/1hVzk_JcNFx-6), 2023. 

+ **NMR, x-ray and Mössbauer results for amorphous Li-Si alloys using density 
functional tight-binding method**. <ins>F. Fernandez</ins>, M. Otero,
M. B. Oviedo, D. E. Barraco, S. A. Paz, E. P. M. Leiva. 
[_Physical Review B_](https://doi.org/10.1103/PhysRevB.108.144201), 2023.
([_preprint arXiv:2305.11006_](https://arxiv.org/abs/2305.11006)).

+ **Density functional tight-binding model for Lithium-Silicon alloys**. B. 
Oviedo, <ins>F. Fernandez</ins>, M. Otero, E. Leiva, A. Paz. [_The Journal of 
Physical Chemistry A_](https://doi.org/10.1021/acs.jpca.3c00075), 2023. 
([_preprint ChemRxiv_](https://doi.org/10.26434/chemrxiv-2022-5s955), 2022).

+ **Characterization of amorphous Li<sub>x</sub>Si structures from ReaxFF via
accelerated exploration of local minima**. <ins>F. Fernandez</ins>, A. Paz, 
M. Otero, D. Barraco, E. Leiva. [_Physical Chemistry Chemical 
Physics_](https://doi.org/10.1039/D1CP02216D), 2021.


### Conference presentations

+ 2nd Renewable energy workshop: lithium batteries and hydrogen. _Córdoba, 
Argentina_. Oct, 2023. Poster: "A heuristic model based on galvanostatic 
simulations for fast charging of lithium-ion battery electrodes".

+ Y-TEC PHD candidates exhibition. _La Plata, Argentina_. Sep, 2023. Poster:
"Fast-charging lithium-ion batteries: A heuristic model to predict optimal 
particle size".

+ 8th Meeting of Young Researchers in Materials Science and Technology. _Córdoba,
Argentina_. Sep, 2023. Poster: "Nearest-neighbor model for predicting 7Li 
chemical shift spectra in Si anodes".

+ 34th Topical Meeting of the International Society of Electrochemistry. _Mar del 
Plata, Argentina_. Mar 20-22, 2023. 
    - Poster: "Study of electrochemical properties in the lithiation of an 
    amorphous silicon structure using a DFTB potential".
    - Talk: "Galvanostatic maps for fast-charging diagnosis of active materials 
    in LIBs", _co-author_.

+ 107th Argentine Physics Association Meeting. _Bariloche, Argentina_. 
Sep 27--30, 2022.
    - Talk: "Development of lithium-ion battery materials: Computational physics 
    applied to the optimization of silicon anodes".
    - Poster: "DFT study of amorphous and crystalline structures of LiSi and 
    LiSn", _co-author_. 

+ XXI Meeting of surfaces and nanostructured materials. _Río Cuarto, Argentina_. 
Aug 9--11, 2022. Poster Flash: "Short range order of amorphous structures in
silicon anodes using a semiempirical reactive potential". (**Best poster flash 
award**).

+ 1st National Lithium Meeting. _Argentina/Online_. Dec 1-3, 2021. Poster: 
"Electrochemical and structural behavior of silicon anodes based on computational 
simulations".

+ 8th International Workshop on Lithium, Industrial Minerals and Energy (IWLiME).
_Cochabamba, Bolivia/Online_. Nov 8-10, 2021. Poster: "Amorphous Li-Si structures 
found via a novel simulation method using a reactive force field". 

+ 72nd Annual Meeting of the International Society of Electrochemistry. 
_Jeju Island, Korea/Online_. Aug 29-Sep 3, 2021. Talk: "Kinectic modeling on 
lithium-ion instertion in prototypical systems", _co-autor_.

+ XII Argentina Congress of Physical Chemistry and Inorganic Chemistry. _La 
Plata, Argentina/Online_. Aug 19-29, 2021. Talk: "A journey through the nanoworld 
of Li batteries", _co-author_.

+ 7th IWLiME. _Antofagasta, Chile/Online_. Nov 9-11, 2020. Poster: "First steps 
towards reproducing chemical shifts spectra of c-LiSi alloys using a 
semi-empirical force field".

+ Workshop on scientific programming techniques. _Córdoba, Argentina_. Jul 15–26, 2019.


## License

Modelado computacional para el desarrollo de electrodos de baterías de ion-litio 
de próxima generación © 2024 by Francisco Fernandez is licensed under 
[Attribution-ShareAlike 4.0 International](http://creativecommons.org/licenses/by-sa/4.0/)
