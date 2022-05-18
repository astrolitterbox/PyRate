import sys
clade = sys.argv[1]
path = "/home/opit/Palaeo/PyRate/data/"
chain = sys.argv[2]
burnin = sys.argv[3]
cutoff = sys.argv[4]


#Move this script to your PyRate root directory
#Usage: python3 print_PyRate_analysis_commands.py <clade> <path> <chain> <burnin> <cutoff factor>

#print("python3 PyRate.py -mProb "+path+clade+"/"+clade+"_"+chain+"rj_mcmc.log -b "+burnin+" > "+path+clade+"/"+clade+"_mProb.txt")


#Extinction-origination plots
print("python3 PyRate.py -plotRJ "+path+clade+"/ -tag "+clade+" -grid_plot 1 &&") 

print("Rscript "+path+clade+"/RTT_plots.r"+" &&")

print("python3 PyRate.py -ginput "+path+clade+"/ -tag "+clade+" -b "+burnin+" &&")

print("python3 PyRate.py -d "+path+clade+"/"+clade+"_"+chain+"rj_se_est.txt -ltt 1 &&")

print("Rscript "+path+clade+"/"+clade+"_"+chain+"rj_se_est_ltt.R &&")
print("Rscript "+path+clade+"/"+clade+"_"+chain+"rj_mcmc_LTT.r &&")

print("python3 PyRate.py -plotQ "+path+clade+"/"+clade+"_"+chain+"rj_mcmc.log -qShift data/stages.txt -b "+burnin+" &&")

print("Rscript "+path+clade+"/"+clade+"_"+chain+"rj_mcmc_RTT_Qrates.r")

for i in range(1, int(chain)+1):
	print("python3  "+path+"analyze_MCMC.py "+clade+" "+str(i)+" "+burnin+" "+cutoff)#+" > "+path+clade+"/"+clade+"_ess.txt")


