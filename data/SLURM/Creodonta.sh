#!/bin/bash
#SBATCH --account=alloc_4061f_vu70412vult
#SBATCH -o Creo.out  
#SBATCH -p main 
#SBATCH --job-name="Creo"
#SBATCH -t 8:00:00
#SBATCH --ntasks=1
#SBATCH --array=2-20
SIM=$SLURM_ARRAY_TASK_ID
srun singularity exec python.sif python3 $HOME/PyRate/PyRate.py $HOME/PyRate/data/Creodonta_PyRate.py -A 4 -n 40000000 -s 10000 -qShift $HOME/PyRate/data/stages.txt -M 5 -pP 1.5 0 -j $SIM
