# vmd -e config.tcl x-Si.xyz
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

mol representation VDW
