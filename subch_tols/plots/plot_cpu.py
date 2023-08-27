import matplotlib.pyplot as plt
import numpy as np

sdc_files = [
#    ("subch_sdc_cfl0.4/cpu_times.out", "SDC CFL=0.4", "C0", "+"),
    ("subch_sdc/cpu_times.out", "SDC-0.2", "k", None),
    ("subch_sdc_cfl0.4/cpu_times.out", "SDC-0.4", "0.5", None),
    ]

strang_files = [
    ("subch_strang/cpu_times.out", "Strang-0.2", "C0", "o"),
#    ("subch_strang_cfl0.1/cpu_times.out", "Strang CFL=0.1", "C1", "x"),
#    ("subch_strang_noTevolve_fix/cpu_times.out", "Strang, CFL=0.2, no T evolution", "C2", "s"),
    ("subch_strang_cfl0.05/cpu_times.out", "Strang-0.05", "C0", "+"),
#    ("subch_strang_tol1e-6/cpu_times.out", "Strang-tol1", "C1", "^"),
    ("subch_strang_tol1.e-8/cpu_times.out", "Strang-tol", "C1", "x")]

fig, ax = plt.subplots()

for diag_file, label, color, ls in sdc_files + strang_files:
    data = np.genfromtxt("subch_diags/" + diag_file)

    ax.plot(data[:,1], data[:,2]/8, label=label, color=color, marker=ls, markevery=0.025)

ax.legend(fontsize="medium")
ax.set_xlim(0.0, 1.0)

ax.grid(linestyle=":", which="both")

ax.set_xlabel("time (s)")
ax.set_ylabel("node hours")
fig.set_size_inches((6, 6))
fig.tight_layout()
fig.savefig("subch_cpu.pdf")
