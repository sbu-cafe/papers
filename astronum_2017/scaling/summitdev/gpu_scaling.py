import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams.update({'font.size': 14})

data = np.loadtxt("starlord-2017-10-05.txt")

nodes = data[:,0]
GPUs = data[:,1]
probsize = data[:,2]
FOM = data[:,3]

num_gpus = nodes*GPUs

plt.scatter(num_gpus, FOM)

plt.xlabel("# of GPUs", fontsize="medium")
plt.ylabel(r"zones/$\mu$s updated", fontsize="medium")

plt.tight_layout()
plt.savefig("summitdev_scaling.pdf")
