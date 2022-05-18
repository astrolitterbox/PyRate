#!/bin/bash
#SBATCH --account=alloc_4061f_vu70412vult
#SBATCH -o Carn.out  
#SBATCH -p main 
#SBATCH --job-name="Carn"
#SBATCH -t 7-0
#SBATCH --ntasks=1
#SBATCH --array=1
SIM=$SLURM_ARRAY_TASK_ID
srun singularity exec python.sif python3 $HOME/PyRate/PyRate.py $HOME/PyRate/data/Carnivora_PyRate.py -A 4 -n 300000000 -s 10000 -qShift $HOME/PyRate/data/stages.txt -pP 1.5 0 -j $SIM
