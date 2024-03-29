import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.axes_grid1.inset_locator import (InsetPosition, inset_axes,
                                                   mark_inset)

sdc_files = [
#    ("subch_sdc_cfl0.4/species_diag.out", "SDC CFL=0.4", "C0", "+"),
    ("subch_sdc/species_diag.out", "SDC-0.2", "k", None),
    ("subch_sdc_cfl0.4/species_diag.out", "SDC-0.4", "0.5", None),
    ]

strang_files = [
    ("subch_strang/species_diag.out", "Strang-0.2", "C0", "o"),
#    ("subch_strang_cfl0.1/species_diag.out", "Strang CFL=0.1", "C1", "x"),
#    ("subch_strang_noTevolve_fix/species_diag.out", "Strang, CFL=0.2, no T evolution", "C2", "s"),
    ("subch_strang_cfl0.05/species_diag.out", "Strang-0.05", "C0", "+"),
#    ("subch_strang_tol1e-6/species_diag.out", "Strang-tol1", "C1", "^"),
    ("subch_strang_tol1.e-8/species_diag.out", "Strang-tol", "C1", "x")]

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

    mass = data[:,15] + data[:,16] + data[:,17] + data[:,18] + data[:,19] + data[:,20]
    ax.plot(data[:,1], mass, label=label, color=color, marker=ls, markevery=0.025)

ax.legend(fontsize="medium")
ax.set_xlim(0.0, 1.0)
ax.set_ylim(1.e-3, 1.0)
ax.set_yscale("log")

ax.grid(linestyle=":", which="both")

ax.set_xlabel("time (s)")
ax.set_ylabel("intermediate nuclei mass (solar masses)")

# Create a set of inset Axes: these should fill the bounding box allocated to
# them.
ax2 = plt.axes([0,0,1,1])
# Manually set the position and relative size of the inset axes within ax1
ip = InsetPosition(ax, [0.16,0.40,0.4,0.35])
ax2.set_axes_locator(ip)
# Mark the region corresponding to the inset axes on ax1 and draw lines
# in grey linking the two axes.
mark_inset(ax, ax2, loc1=1, loc2=3, fc="none", ec='0.5')

for diag_file, label, color, ls in sdc_files + strang_files:
    data = monotonize(np.loadtxt("subch_diags/" + diag_file))

    mass = data[:,15] + data[:,16] + data[:,17] + data[:,18] + data[:,19] + data[:,20]
    ax2.plot(data[:,1], mass, label=label, color=color, marker=ls, markevery=0.15)

ax2.set_xlim(0.73, 0.7875)
ax2.set_yscale("log")
ax2.set_ylim(0.006, 0.01)


fig.set_size_inches((6, 6))
fig.tight_layout()
fig.savefig("subch_intermediate.pdf")
