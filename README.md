# Computational simulations for next-generation lithium-ion battery electrode development

PhD at [FAMAF](https://www.famaf.unc.edu.ar/), working in the computational area 
of [LAES](http://www.laesunc.com/laes/).

Advisors: Prof. Dr. Daniel Barraco & Prof. Dr. Ezequiel Leiva


## Abstract (abbreviated version)

TODO


## PhD requirements fulfilled

### Dissertation

TODO

### PhD seminars talks

+ **Machine learning interatomic potentials and their application to lithium 
batteries**. Apr 22, 2022. _Aula Magna, FAMAF._ 

+ 2 nd seminar talk: TODO

### Postgraduate courses

+ [Software design for scientific computing](https://github.com/leliel12/diseno_sci_sfw), 
FAMAF, UNC. 60 hrs, 2021.

+ [Parallel computing](https://cs.famaf.unc.edu.ar/~nicolasw/Docencia/CP/2020/index.html),
FAMAF, UNC. 120 hrs, 2020.

+ [Computational physics](https://github.com/fernandezfran/fiscomp), FAMAF, UNC. 
120 hrs, 2020.

+ Nuclear magnetic resonance, FAMAF, UNC. 25 hrs, 2020.

+ Computer simulations in condensed matter systems, FCQ, UNC. 40 hrs, 2019.

+ Electrochemistry, FCQ, UNC. 80 hrs, 2019.

### Extra postgraduate courses

These courses were not part of the formal requirements for the PhD, but they 
contributed to my training and the concepts covered have been used throughout 
my research.

+ Machine Learning School for Materials @ Ilum, CNPEM. 20 hrs, Sep 5--7, 2022.

+ Machine learning for scarse data, ECI, DC, UBA. 15 hrs, Jul 26--30, 2021.

+ [Python programming](https://github.com/python-unsam/Programacion_en_Python_UNSAM),
ECyT, UNSAM. 96 hrs, 2021.


## Research activity

### Scientific articles

+ **UMBEM: A Universal Metric for Benchmarking fast-charging Electrode Materials**.
<ins>F. Fernandez</ins> _et al_. _Mnuscript in preparation_, 2023.

+ **Towards a fast-charging of LIBs electrode materials: a heuristic model based 
on galvanostatic simulations**. <ins>F. Fernandez</ins>, E. M. Gavilán-Arriazu, 
D. E. Barraco, A. Visintín, Y. Ein-Eli, E. P. M. Leiva. _Manuscript 
submitted_, 2023. 

+ **Prediction of NMR, X-ray and Mössbauer experimental results for amorphous 
Li-Si alloys using a novel DFTB model**. <ins>F. Fernandez</ins>, M. Otero, 
M. B. Oviedo, D. E. Barraco, S. A. Paz, E. P. M. Leiva. ([_preprint 
arXiv:2305.11006_](https://arxiv.org/abs/2305.11006), 2023).

+ **Density functional tight-binding model for Lithium-Silicon** B. Oviedo, 
<ins>F. Fernandez</ins>, M. Otero, E. Leiva, A. Paz. [_The Journal of Physical 
Chemistry A_](https://doi.org/10.1021/acs.jpca.3c00075), 2023. ([_preprint 
ChemRxiv_](https://doi.org/10.26434/chemrxiv-2022-5s955), 2022).

+ **Characterization of amorphous Li<sub>x</sub>Si structures from ReaxFF via
accelerated exploration of local minima**. <ins>F. Fernandez</ins>, A. Paz, 
M. Otero, D. Barraco, E. Leiva. [_Physical Chemistry Chemical 
Physics_](https://doi.org/10.1039/D1CP02216D), 2021.


### Conference presentations

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

+ 1 st National Lithium Meeting. _Argentina/Online_. Dec 1-3, 2021. Poster: 
"Electrochemical and structural behavior of silicon anodes based on computational 
simulations".

+ 8 th International Workshop on Lithium, Industrial Minerals and Energy (IWLiME).
_Cochabamba, Bolivia/Online_. Nov 8-10, 2021. Poster: "Amorphous Li-Si structures 
found via a novel simulation method using a reactive force field". 

+ 72 nd Annual Meeting of the International Society of Electrochemistry. 
_Jeju Island, Korea/Online_. Aug 29-Sep 3, 2021. Talk: "Kinectic modeling on 
lithium-ion instertion in prototypical systems", _co-autor_.

+ XII Argentina Congress of Physical Chemistry and Inorganic Chemistry. _La 
Plata, Argentina/Online_. Aug 19-29, 2021. Talk: "A journey through the nanoworld 
of Li batteries", _co-author_.

+ 7 th IWLiME. _Antofagasta, Chile/Online_. Nov 9-11, 2020. Poster: "First steps 
towards reproducing chemical shifts spectra of c-LiSi alloys using a 
semi-empirical force field".

+ Workshop on scientific programming techniques. _Córdoba, Argentina_. Jul 15–26, 2019.


## Instructions to generate the thesis

The thesis is compiled using the Makefile:
```
cd src/
make clean && make
xdg-open thesis.pdf
```


## Disclaimer

This repo may not faithfully reflect the final version of the PhD thesis in its 
entirety.


## LICENSE

https://creativecommons.org/licenses/by-nc-nd/4.0/
