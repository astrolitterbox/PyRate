#!/bin/bash
#SBATCH --account=alloc_4061f_vu70412vult
#SBATCH -o Ancient.out  
#SBATCH -p main 
#SBATCH --job-name="Ancie"
#SBATCH -t 08:00:00
#SBATCH --ntasks=1
#SBATCH --array=2-20
SIM=$SLURM_ARRAY_TASK_ID
srun singularity exec python.sif python3 $HOME/PyRate/PyRate.py $HOME/PyRate/data/Ancient_mammals_PyRate.py -A 4 -n 20000000 -s 2000 -qShift $HOME/PyRate/data/stages.txt -pP 1.5 0 -j $SIM -M 5 -restore_mcmc=$HOME/PyRate/data/pyrate_mcmc_logs/Ancient_mammals_${SIM}rj_mcmc.log
