# LAMMPS_Templates
This holds scripts that template different Molecular Dynamics Jobs using the LAMMPS Software.

# Larger Goals in order of priority:

## Combine/make data files

Data files hold molecular information. At some point it would be nice to be able to make datafiles given an xyz file but for now I am using a tool on nano hub to generate the files. These files contain all the information needed, but atoms, bond types, and etc may have different labels and these need to be labeled the same if the molecules are to be placed randomely in a box.

## Initialize the simulations

This is a difficult thing to do as there are different kinds of jobs, sometimes you are running from a previous job, there are different types of units, for now I will be making this pack a random box and running reaxff jobs with another forcefield. Other functionality can be added as needed.

## Set up NVT and NPT Steps

This will likely just be done using formatable strings until the need arises to change that.
