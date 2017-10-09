import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({'xtick.labelsize': 14,
                     'ytick.labelsize': 14,
                     'font.size': 14})

plt.rc("axes", linewidth=1.5)
plt.rc("lines", markeredgewidth=1.5)


data = np.loadtxt("starlord-2017-10-05.txt")

nodes = data[:,0]
GPUs = data[:,1]
probsize = data[:,2]
FOM = data[:,3]

num_gpus = nodes*GPUs


plt.scatter(num_gpus, FOM)
plt.plot(num_gpus, num_gpus/num_gpus[0]*FOM[0], ls=":")
plt.xlabel("number of GPUs", fontsize="medium")
plt.ylabel(r"zones/$\mu$s updated", fontsize="medium")

ax = plt.gca()
plt.text(0.95, 0.95, "StarLord GPU performance", 
         fontsize="small", horizontalalignment="right", transform = ax.transAxes)


plt.tight_layout()

f = plt.gcf()
f.set_size_inches(8, 6)

plt.savefig("summitdev_scaling.pdf", dpi=150, bbox_inches="tight")
