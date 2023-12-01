# Copyright (c) 2024, Francisco Fernandez
# License: CC BY-SA 4.0
#   https://github.com/fernandezfran/thesis/blob/main/LICENSE
#
# tcl script for configure crystall and amorphous Si in VMD, it wraps the atom
# position to the simulation cell using periodic boundary conditions, run the 
# following command:
#   $ vmd -e config.tcl x-Si.xyz
display projection Orthographic

axes location off

color Display Background white

pbc set {10.937456 10.937456 10.937456} -all
pbc wrap -all

pbc box -color gray

color change rgb blue 0.121569 0.466667 0.705882
color Name S blue

mol delrep 0 0

mol representation VDW 0.2 32
mol selection all
mol addrep 0

mol representation DynamicBonds 3.0 0.1 32
mol selection all
mol addrep 0
