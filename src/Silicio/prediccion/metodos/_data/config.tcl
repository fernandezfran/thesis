# $ vmd -e config.tcl config.lammpstrj
display projection Orthographic

axes location off

color Display Background white

pbc box -color gray

color change rgb blue 0.121569 0.466667 0.705882
color Name 1 blue
color change rgb green 0.172549 0.627451 0.172549
color Name 2 green

set silicios [atomselect top "type == 1"]
set litios [atomselect top "type == 2"]

$silicios set radius 0.3
$litios set radius 0.2

mol representation VDW
