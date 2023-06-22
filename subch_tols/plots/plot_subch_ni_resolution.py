import matplotlib.pyplot as plt
import numpy as np

sdc_files = [
    ("subch_sdc_40km/species_diag.out", "SDC 40 km"), 
    ("subch_sdc/species_diag.out", "SDC 20 km"), 
    ("subch_sdc_10km_3lev/species_diag.out", "SDC 10 km"), 
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

fig.set_size_inches((8, 8))
fig.savefig("subch_ni56_res.pdf")
