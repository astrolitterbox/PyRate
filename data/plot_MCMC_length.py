import matplotlib.pyplot as plt
import numpy as np

clade = ["Creodonta", "Proboscidea", "Ancient", "Perissodactyla", "Carnivora", "Artiodactyla"]
species = np.asarray([151, 173, 562, 738, 1107, 1670])
#time = [6.5, ]
length = np.asarray([40, 20, 20, 300, 300, 340])
ess = [1300, 357, 244, 341, 92, 15]

samples_per_species = length*1000./species

#y = 0.49557522123894x – 65.734513274336
#From this eq: Artiodactyla should have 800M samples, if relation is linear..let's wait until it finishes


plt.scatter(species, length)
for s,l, c in zip(species,length, clade):
    label = f"{c}"
    plt.annotate(label, # this is the text
                 (s,l), # these are the coordinates to position the label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center

plt.axline((0, -65), slope=0.5, color='k', label='ESS ~ 300')

plt.xlabel("No. of species")
plt.ylabel("MCMC chain length, Msamples")
plt.ylim(0, 800)
plt.savefig("MCMC_diagnostics/species_vs_length.png")

plt.clf()

plt.scatter(samples_per_species, ess)
for s,l, c in zip(samples_per_species, ess, clade):
    label = f"{c}"
    plt.annotate(label, # this is the text
                 (s,l), # these are the coordinates to position the label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='left') # horizontal alignment can be left, right or center
plt.axhline(100, c='k')

plt.xlabel("Samples per species, x 1000")
plt.ylabel("ESS")
plt.savefig("MCMC_diagnostics/ESS_per_species.png")


plt.clf()

plt.scatter(length, ess)
for s,l, c in zip(length, ess, clade):
    label = f"{c}"
    plt.annotate(label, # this is the text
                 (s,l), # these are the coordinates to position the label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='left') # horizontal alignment can be left, right or center

plt.axhline(100, c='k')
plt.xlabel("Chain length, Msamples")
plt.ylabel("ESS")
plt.savefig("MCMC_diagnostics/ESS_vs_length.png")

