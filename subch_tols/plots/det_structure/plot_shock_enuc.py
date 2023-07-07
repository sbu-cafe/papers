import matplotlib.pyplot as plt
import numpy as np
from matplotlib import ticker

d10 = np.loadtxt("subch_sdc_10km_3lev_plt17526.slice")
d20 = np.loadtxt("subch_sdc_20km_plt17412.slice")
d40 = np.loadtxt("subch_sdc_40km_plt17272.slice")

fig, ax = plt.subplots()

ax.set_yscale("symlog", linthresh=1.e10)

ax.plot(d10[:,0], d10[:,3], label="10 km")
ax.plot(d20[:,0], d20[:,3], label="20 km")
ax.plot(d40[:,0], d40[:,3], label="40 km")

ax.set_xlim(0, 1.2e8)
ax.legend()

ax.xaxis.set_major_formatter(ticker.ScalarFormatter(useMathText=True))
ax.grid(linestyle=":")

ax.set_xlabel("r [cm]")
ax.set_ylabel("nuclear energy generation rate [erg/g/s]")

fig.set_size_inches(6, 8)

fig.tight_layout()
fig.savefig("det_structure.pdf")
