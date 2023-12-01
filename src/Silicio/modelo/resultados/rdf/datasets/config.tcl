# Copyright (c) 2024, Francisco Fernandez
# License: CC BY-SA 4.0
#   https://github.com/fernandezfran/thesis/blob/main/LICENSE
#
# tcl script for configure crystall and amorphous Si in VMD, it wraps the atom
# position to the simulation cell using periodic boundary conditions, run the 
# following command:
#   $ vmd -e config.tcl x-Si.xyz
#
# Note: above each tcl command is the explanation of how it would be done in 
# the VMD GUI.

# Display > Ortographic 
display projection orthographic

# Display > Axes > Off
axes location off

# Graphics > Colors > Categories > Display
#                   > Names > Background
#                   > Colors > 8 white
color Display Background white

# Define the a, b and c of periodic boundary conditions in all frames of the
# .xyz trajectory (note that this is valid only for simulations with fixed 
# volume, e.g. NVT ensemble)
pbc set {10.937456 10.937456 10.937456} -all

# then all the positions are wrapped inside the box
pbc wrap -all

# and it is displayed with gray color
pbc box -color gray

# Graphics > Colors > Categories > Name
#                   > Names > S
#                   > Colors > 0 blue
# edit the RGB of 0 blue with this values
color change rgb blue 0.121569 0.466667 0.705882
color Name S blue

# Insted of delete actual representation, modify:
# Graphics > Representations >
#                        Selected Atoms > all
#                        Drawning Method > VDW
#                          Sphere Scale 0.2
#                          Sphere Resolution 32
mol delrep 0 0

mol representation VDW 0.2 32
mol selection all
mol addrep 0

# Graphics > Representations > Create Rep >
#                                  Selected Atoms > all
#                                  Drawning Method > DynamicBonds
#                                    Distance Cutoff 3.0
#                                    Bond Radius 0.1
#                                    Bond Resolution 32
mol representation DynamicBonds 3.0 0.1 32
mol selection all
mol addrep 0
