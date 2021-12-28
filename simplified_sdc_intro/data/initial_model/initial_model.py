# take a raw inputs file for aprox21 and convert to the aprox19
# nuclei.  This means getting rid of Cr56 and Fe56 (by lumping them
# into Ni56)

import numpy as np
import matplotlib.pyplot as plt

def find_r_for_rho(r, rho, rho_want):
    idx = np.where(rho < rho_want)[0][0]
    return r[idx]


#file = "../15m_500_sec.aprox19.hse.6400"
file = "sub_chandra.M_WD-1.10.M_He-0.050.hse.C.N14.5.000km"
Lx = 1.024e9

data = np.loadtxt(file)

print(data.shape)

# now manually read to get the variable names

# the first column is position

names = ["r"]

with open(file) as f:
    for n, line in enumerate(f):
        if line.startswith("# num"):
            continue

        if line.startswith("# npts"):
            continue

        if not line.startswith("#"):
            break

        names.append(line.split()[-1].strip())

# now make plots

idens = names.index("density")
itemp = names.index("temperature")

fig = plt.figure()
ax = fig.add_subplot(211)

l1 = ax.plot(data[:,0], data[:,idens], label="density", lw=2)
l2 = ax.plot(data[:,0], data[:,itemp], label="temperature", lw=2)

ax.set_xscale("log")
ax.set_yscale("log")

ax.set_xlabel("r [cm]")
ax.set_ylabel(r"$\rho~[\rm{g/cm^3}]$, $T~[K]$")

ax.legend(frameon=False)


ax = fig.add_subplot(212)

threshold = 0.001


for n, var in enumerate(names):
    print(n, var)

    if var in ["r", "density", "temperature", "pressure"]:
        continue

    Xmax = data[:,n].max()

    lw = 2
    if Xmax > threshold:
        ax.plot(data[:,0], data[:,n], label=var, lw=lw)


ax.set_xscale("log")
ax.set_yscale("log")

ax.set_xlabel("r [cm]")
ax.set_ylabel("mass fraction")

ax.legend(frameon=False)

fig.set_size_inches((8, 10))

fig.tight_layout()

fig.savefig("initial_model.pdf")

