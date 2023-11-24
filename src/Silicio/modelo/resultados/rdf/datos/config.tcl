# tcl script for configure crystall and amorphous Si in VMD, it wraps the atom
# position to the simulation cell using periodic boundary conditions, run the 
# following command:
#   $ vmd -e config.tcl x-Si.xyz
display projection Orthographic

axes location off

color Display Background white

molinfo 0 set a 10.937456
molinfo 0 set b 10.937456
molinfo 0 set c 10.937456

pbc wrap

pbc box -color gray

color change rgb blue 0.121569 0.466667 0.705882
color Name S blue

$silicios set representation {DynamicBonds 3.0 0.1 32}
$silicios set representation {VDW 1.0 32}
$litios set representation {VDW 1.0 32}
