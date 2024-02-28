# Copyright (c) 2024, Francisco Fernandez
# License: CC BY-SA 4.0
#   https://github.com/fernandezfran/thesis/blob/main/LICENSE
#
# tcl script for configure LiSi systems in VMD, run the following command:
#   $ vmd -e config.tcl config.lammpstrj
#
# Note: above each tcl command is the explanation of how it would be done in 
# the VMD GUI.
# Also note: you can copy this scripts to the following paths or open then 
# from here
#   prediccion/metodos/datasets/
#   caracterizacion/resultados/introduccion/amorfas/
#   caracterizacion/metodos/config/cristalinas/datasets/

# Display > Ortographic 
display projection orthographic

# Display > Axes > Off
axes location off

# box must be defined in the lammpstrj file to run this line
pbc box -color gray

# Graphics > Colors > Categories > Display
#                   > Names > Background
#                   > Colors > 8 white
color Display Background white

# Graphics > Colors > Categories > Name
#                   > Names > 1
#                   > Colors > 0 blue
# edit the RGB of 0 blue with this values
color change rgb blue 0.121569 0.466667 0.705882
color Name 1 blue

# Graphics > Colors > Categories > Name
#                   > Names > 2
#                   > Colors > 7 green
# edit the RGB of 7 green with this values
color change rgb green 0.172549 0.627451 0.172549
color Name 2 green

# the following 4 cmds allows to make only two representations, in GUI
# there is one more
set silicios [atomselect top "type == 1"]
set litios [atomselect top "type == 2"]
$silicios set radius 0.3
$litios set radius 0.2

# Insted of delete actual representation, modify:
# Graphics > Representations >
#                        Selected Atoms > type 2
#                        Drawning Method > VDW
#                          Sphere Scale 0.2
#                          Sphere Resolution 32
mol delrep 0 0

# Graphics > Representations > Create Rep >
#                                  Selected Atoms > type 1
#                                  Drawning Method > VDW
#                                    Sphere Scale 0.3
#                                    Sphere Resolution 32
mol representation VDW 1.0 32
mol selection all
mol addrep 0

# Graphics > Representations > Create Rep >
#                                  Selected Atoms > type 1
#                                  Drawning Method > DynamicBonds
#                                    Distance Cutoff 3.0
#                                    Bond Radius 0.1
#                                    Bond Resolution 32
mol representation DynamicBonds 3.0 0.1 32
mol selection {type 1}
mol addrep 0
