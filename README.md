# PyRate
Various scripts for Bayesian paleodiversity analysis

PyRate_todo.txt describes the PyRate analysis process starting with fossil input file generation from NOW database (1: write_Pyrate_input.py), PyRate input scripts creation with PyRate R utility (2), SLURM batch scripts (3), uploading these and auxilliary files to the server (4), running SLURM job arrays (5), downloading the PyRate MCMC chains and other output files (6), generating native PyRate and Arviz analysis script calls (7):

python3 print_PyRate_analysis_commands.py <cutoff -- fraction of MCMC samples to be removed from the end of the chain, use 0 for full chain>
