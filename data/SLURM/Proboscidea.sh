#!/bin/bash
#SBATCH --account=alloc_4061f_vu70412vult
#SBATCH -o Prob.out  
#SBATCH -p main 
#SBATCH --job-name="Prob"
#SBATCH -t 1:10:00
#SBATCH --ntasks=1
#SBATCH --array=2,4-20
SIM=$SLURM_ARRAY_TASK_ID
srun singularity exec python.sif python3 $HOME/PyRate/PyRate.py $HOME/PyRate/data/Proboscidea_PyRate.py -A 4 -n 6000000 -s 10000 -qShift $HOME/PyRate/data/stages.txt -pP 1.5 0 -j $SIM -M 5
