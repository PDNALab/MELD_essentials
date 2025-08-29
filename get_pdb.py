# a small script to extract the initial PDB from a MELD system

import pickle

# Load MELD system
with open('Data/system.dat', 'rb') as f:
    system = pickle.load(f)


# Get the PDB writer
pdb_writer = system.get_pdb_writer()
coord = system.template_coordinates

with open("initial.pdb", "w") as out:
    out.write(pdb_writer.get_pdb_string(coord, 0))

