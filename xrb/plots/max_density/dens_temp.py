import numpy as np
import matplotlib.pyplot as plt
import glob

for filename in glob.glob("*.out"):
    data = np.loadtxt(filename)

    plt.plot(data[:,0], data[:,2]/data[0,2], label="{}".format(filename.split(".")[0]))


plt.ylim(1.0, 1.4)
plt.legend(fontsize="small", frameon=False)

plt.savefig("max_dens.png")

plt.clf()

for filename in glob.glob("*.out"):
    data = np.loadtxt(filename)
    if len(data[0,:]) == 5:
        plt.plot(data[:,0], data[:,4]/data[0,4], label="{}".format(filename.split(".")[0]))


plt.ylim(0.6, 1.4)
plt.legend(fontsize="small", frameon=False)

plt.savefig("max_temp.png")
