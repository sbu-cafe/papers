import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

# Use LaTeX for rendering
mpl.rcParams["text.usetex"] = True
# load the xfrac package
mpl.rcParams["text.latex.preamble"] += r'\newcommand{\isotm}[2]{{}^{#2}\mathrm{#1}}'
mpl.rcParams['mathtext.fontset'] = 'cm'
mpl.rcParams['mathtext.rm'] = 'serif'

###
### NOTE: the data in these files is in solar masses!
###

fig, ax = plt.subplots()

data3d = np.loadtxt("flame_wave_3d_nonsquare_cool/species_diag.out")
total_mass = np.sum(data3d[:,2:8])

print(f"total mass 3d = {total_mass}")
print(f"total He mass 3d = {data3d[0, 2]}, {data3d[-1, 2]}")

mass_He0 = data3d[0, 2]

ax.plot(data3d[:,1], data3d[:,2] / mass_He0, label=r"$\isotm{He}{4}$", color="C0")
ax.plot(data3d[:,1], data3d[:,3] / mass_He0, label=r"$\isotm{C}{12}$", color="C1")
ax.plot(data3d[:,1], data3d[:,4] / mass_He0, label=r"$\isotm{O}{16}$", color="C2")
ax.plot(data3d[:,1], data3d[:,5] / mass_He0, label=r"$\isotm{Ne}{20}$", color="C3")
ax.plot(data3d[:,1], data3d[:,6] / mass_He0, label=r"$\isotm{Mg}{24}$", color="C4")
ax.plot(data3d[:,1], data3d[:,7] / mass_He0, label=r"$\isotm{Si}{28}$", color="C5")
ax.plot(data3d[:,1], data3d[:,8] / mass_He0, label=r"$\isotm{Ni}{56}$", color="C6")


data2d = np.loadtxt("flame_wave_2d_nonsquare_cool_new/species_diag.out")
mass_He0 = data2d[0, 2]


ax.plot(data2d[:,1], data2d[:,2] / mass_He0, linestyle="--", color="C0")
ax.plot(data2d[:,1], data2d[:,3] / mass_He0, linestyle="--", color="C1")
ax.plot(data2d[:,1], data2d[:,4] / mass_He0, linestyle="--", color="C2")
ax.plot(data2d[:,1], data2d[:,5] / mass_He0, linestyle="--", color="C3")
ax.plot(data2d[:,1], data2d[:,6] / mass_He0, linestyle="--", color="C4")
ax.plot(data2d[:,1], data2d[:,7] / mass_He0, linestyle="--", color="C5")
ax.plot(data2d[:,1], data2d[:,8] / mass_He0, linestyle="--", color="C6")

ax.set_yscale("log")
ax.legend()

ax.set_xlabel("time (s)")
ax.set_ylabel("mass / initial He mass")

ax.set_xlim(0.0, 0.04)

fig.set_size_inches(7.0, 7.0)

fig.tight_layout()
fig.savefig("mass_plot.pdf")

