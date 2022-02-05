import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

# Use LaTeX for rendering
mpl.rcParams["text.usetex"] = True
# load the xfrac package
mpl.rcParams["text.latex.preamble"] += r'\newcommand{\isotm}[2]{{}^{#2}\mathrm{#1}}'
mpl.rcParams['mathtext.fontset'] = 'cm'
mpl.rcParams['mathtext.rm'] = 'serif'


fig, ax = plt.subplots()

data = np.loadtxt("species_masses_3d.txt")
total_mass = np.sum(data, axis=1)

print(f"total mass 3d = {total_mass[0]}")
print(f"total He mass 3d = {data[0, 1]}, {data[-1, 1]}")

mass_He0 = data[0, 1]

ax.plot(data[:,0], data[:,1] / mass_He0, label=r"$\isotm{He}{4}$", color="C0")
ax.plot(data[:,0], data[:,2] / mass_He0, label=r"$\isotm{C}{12}$", color="C1")
ax.plot(data[:,0], data[:,3] / mass_He0, label=r"$\isotm{O}{16}$", color="C2")
ax.plot(data[:,0], data[:,4] / mass_He0, label=r"$\isotm{Ne}{20}$", color="C3")
ax.plot(data[:,0], data[:,5] / mass_He0, label=r"$\isotm{Mg}{24}$", color="C4")
ax.plot(data[:,0], data[:,6] / mass_He0, label=r"$\isotm{Si}{28}$", color="C5")
ax.plot(data[:,0], data[:,7] / mass_He0, label=r"$\isotm{Ni}{56}$", color="C6")


data2d = np.loadtxt("species_masses_2d.txt")
mass_He0 = data2d[0, 1]


ax.plot(data2d[:,0], data2d[:,1] / mass_He0, linestyle="--", color="C0")
ax.plot(data2d[:,0], data2d[:,2] / mass_He0, linestyle="--", color="C1")
ax.plot(data2d[:,0], data2d[:,3] / mass_He0, linestyle="--", color="C2")
ax.plot(data2d[:,0], data2d[:,4] / mass_He0, linestyle="--", color="C3")
ax.plot(data2d[:,0], data2d[:,5] / mass_He0, linestyle="--", color="C4")
ax.plot(data2d[:,0], data2d[:,6] / mass_He0, linestyle="--", color="C5")
ax.plot(data2d[:,0], data2d[:,7] / mass_He0, linestyle="--", color="C6")

ax.set_yscale("log")
ax.legend()

ax.set_xlabel("time (s)")
ax.set_ylabel("mass / initial He mass")

fig.set_size_inches(7.0, 7.0)

fig.tight_layout()
fig.savefig("mass_plot.png")

