import pandas as pd
import xarray as xr
import numpy as np
np.set_printoptions(threshold=1000)
pd.set_option('display.max_rows', 1000)
import arviz as az
import matplotlib.pyplot as plt
from pprint import pprint
import sys

clade = sys.argv[1]
chain = sys.argv[2]
burnin = sys.argv[3]
cutoff_factor = float(sys.argv[4])



az.rcParams["plot.max_subplots"] = 64
use_vars_stage = ["posterior", "prior", "PP_lik", "BD_lik", "q_0", "q_1", "q_2", "q_3", "q_4", "q_5",  "k_birth", "k_death", "root_age"]
#use_vars_epoch = ["posterior", "prior", "q_0", "q_1", "q_2", "q_3","q_4", "k_birth", "k_death", "root_age"]
#"q_6", "q_7", "q_8", "q_9", "q_10", "q_11", "q_12", "q_13", "q_14", "q_15", "q_16", "q_17",

#data_vars = use_vars_stage[2:]
use_vars = use_vars_stage
data_vars = use_vars

burnin_length = int(burnin)

print(data_vars)


#Rj with sampled prior
data_root = "/home/opit/Palaeo/PyRate/data/"+clade+"/"
img_root = data_root+"img/"
model_name = clade+"_"+chain+"rj_prior"

df =  pd.read_csv(data_root+clade+"_"+chain+"rj_mcmc.log", sep="\t", usecols=use_vars, header=0)
#Resampling 
#df = df.iloc[::100, :]

#Burnin parameters
chain_length = len(df)
cutoff = int(cutoff_factor*(chain_length-burnin_length))

autocorr_length = chain_length-burnin_length-1-cutoff

title = model_name+", "+str(chain_length)+" samples, "+" burnin: "+str(burnin_length)


df["chain"] = 0
df["draw"] = np.arange(len(df), dtype=int)
df = df.set_index(["chain", "draw"])
xdata = xr.Dataset.from_dataframe(df)

dataset = az.InferenceData(posterior=xdata)


    
dataset = dataset.sel(draw=slice(burnin_length, chain_length-cutoff))



ess = az.ess(dataset)
print("Burn-in: "+str(burnin_length))
print(ess)

az.plot_ess(dataset, textsize=8, kind='evolution', min_ess=100)
plt.savefig(img_root+chain+"_ESS.png")


az.plot_ess(

    dataset, kind="local", drawstyle="steps-mid", color="k",

    linestyle="-", marker=None, rug=False, rug_kwargs={"color": "r"}

)
plt.savefig(img_root+chain+"_ESS_local.png")
#plots

data_row = df[data_vars[4:]]

#Parameters plot
fig = plt.figure()
for index, row in data_row.iterrows():
	plt.plot(row, alpha=0.3, color="black")
plt.title(title)	
plt.savefig(img_root+chain+"_parameters.png")

#Trace

az.plot_trace(dataset)
plt.savefig(img_root+chain+"_trace.png")

#Density

az.plot_density(dataset,
    var_names=use_vars,
    shade=0.1,
)
plt.savefig(img_root+chain+"_density.png")

#Pairs plot

az.plot_pair(dataset, var_names=["posterior", "prior", "q_1", "q_2", "q_3", "q_4", "k_birth", "k_death", "root_age"])
plt.savefig(img_root+chain+"_pairs.png")

#Autocorrelation


az.plot_autocorr(dataset, var_names=use_vars, max_lag=autocorr_length)
plt.savefig(img_root+chain+"_autocorr.png")

