import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.axes_grid1.inset_locator import (InsetPosition, inset_axes,
                                                   mark_inset)

sdc_files = [
    ("subch_sdc_40km/species_diag.out", "SDC-40km"), 
    ("subch_sdc/species_diag.out", "SDC-0.2"), 
    ("subch_sdc_10km_3lev/species_diag.out", "SDC-10km"), 
    ("subch_sdc_5km_4lev/species_diag.out", "SDC-5km"), 
    ]


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

for diag_file, label in sdc_files:
    data = monotonize(np.loadtxt("subch_diags/" + diag_file))

    ax.plot(data[:,1], data[:,23], label=label)

ax.legend(fontsize="small")
ax.set_xlim(0.0, 1.0)
ax.set_ylim(1.e-2, 1.0)
ax.set_yscale("log")

ax.grid(linestyle=":", which="both")

ax.set_xlabel("time (s)")
ax.set_ylabel("Ni56 mass (solar masses)")

# Create a set of inset Axes: these should fill the bounding box allocated to
# them.
ax2 = plt.axes([0,0,1,1])
# Manually set the position and relative size of the inset axes within ax1
ip = InsetPosition(ax, [0.15,0.25,0.35,0.35])
ax2.set_axes_locator(ip)
# Mark the region corresponding to the inset axes on ax1 and draw lines
# in grey linking the two axes.
mark_inset(ax, ax2, loc1=1, loc2=3, fc="none", ec='0.5')

for diag_file, label in sdc_files:
    data = monotonize(np.loadtxt("subch_diags/" + diag_file))

    ax2.plot(data[:,1], data[:,23], label=label)

ax2.set_xlim(0.77, 0.7975)
ax2.set_yscale("log")
ax2.set_ylim(0.0175, 0.04)

fig.set_size_inches((8, 8))
fig.savefig("subch_ni56_res.pdf")
