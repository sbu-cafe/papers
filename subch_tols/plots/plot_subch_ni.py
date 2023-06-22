import matplotlib.pyplot as plt
import numpy as np

sdc_files = [
#    ("subch_sdc_cfl0.4/species_diag.out", "SDC CFL=0.4", "C0", "+"),
    ("subch_sdc/species_diag.out", "SDC CFL=0.2", "k", None),
    ]

strang_files = [
    ("subch_strang/species_diag.out", "Strang CFL=0.2", "C0", "o"),
#    ("subch_strang_cfl0.1/species_diag.out", "Strang CFL=0.1", "C1", "x"),
    ("subch_strang_noTevolve_fix/species_diag.out", "Strang, CFL=0.2, no T evolution", "C2", "s"),
    ("subch_strang_cfl0.05/species_diag.out", "Strang CFL=0.05", "C0", "+"),
    ("subch_strang_tol1e-6/species_diag.out", "Strang CFL=0.2, tols=1.e-6", "C1", "^"),
    ("subch_strang_tol1.e-8/species_diag.out", "Strang CFL=0.2, atol_spec=1.e-8", "C1", "x")]

fig, ax = plt.subplots()

def monotonize(arr):
    new_rows = []
    max_t = -1
    for row in arr:
        t = row[0]
        if t > max_t:
            new_rows.append(row)
        max_t = max(t, max_t)

    return np.asarray(new_rows)

for diag_file, label, color, ls in sdc_files + strang_files:
    data = monotonize(np.loadtxt("subch_diags/" + diag_file))

    ax.plot(data[:,1], data[:,23], label=label, color=color, marker=ls, markevery=0.025)

ax.legend(fontsize="small")
ax.set_xlim(0.0, 1.0)
ax.set_ylim(1.e-2, 1.0)
ax.set_yscale("log")

ax.grid(linestyle=":", which="both")

ax.set_xlabel("time (s)")
ax.set_ylabel("Ni56 mass (solar masses)")

fig.set_size_inches((8, 8))
fig.savefig("subch_ni56.pdf")
