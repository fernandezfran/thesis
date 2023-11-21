#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np

from exma.io import writer


def cif2lammpstrj(cif_file, lammpstrj_name):
    """Write the information of a .cif file to a lammpstrj file.

    Parameters
    ----------
    cif_file : str
        the name of the cif file

    lammpstrj_name : str
        the name of the file with the lammpstrj trajectory.
    """
    with open(cif_file, "r") as cif:
        try:
            # cell info
            for i in range(26):
                line = cif.readline()
                if line.startswith("_cell_length_a"):
                    xbox = float(line.split()[1])
                elif line.startswith("_cell_length_b"):
                    ybox = float(line.split()[1])
                elif line.startswith("_cell_length_c"):
                    zbox = float(line.split()[1])

            # positions
            types, x, y, z = [], [], [], []
            while True:
                line = cif.readline().split()
                types.append(line[0])
                x.append(float(line[3]))
                y.append(float(line[4]))
                z.append(float(line[5]))

        except (EOFError, IndexError):
            ...

    with writer.LAMMPS(lammpstrj_name) as lmp:
        lmp.write_frame(
            {
                "natoms": len(types),
                "box": np.array([xbox, ybox, zbox]),
                "id": np.arange(1, len(types) + 1),
                "type": np.array([1 if e == "Si" else 2 for e in types]),
                "x": xbox * np.array(x),
                "y": ybox * np.array(y),
                "z": zbox * np.array(z),
            }
        )


if __name__ == "__main__":
    import sys

    cif2lammpstrj(sys.argv[1], sys.argv[2])
