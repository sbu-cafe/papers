import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({'xtick.labelsize': 14,
                     'ytick.labelsize': 14,
                     'font.size': 14})

plt.rc("axes", linewidth=1.5)
plt.rc("lines", markeredgewidth=1.5)

class ScalingRun(object):
    def __init__(self, MPI=1, OMP=1, max_grid=1, nzones=1, max_level=1, time=0.0, std=0.0):
        self.MPI = MPI
        self.OMP = OMP
        self.cores = MPI * OMP
        self.max_grid = max_grid
        self.nzones = nzones
        self.max_level = max_level
        self.time = time
        self.std = std


def trend_line(c, t):
    trend = t[0]*c[0]/c[:]
    return trend

runs = []

data = np.loadtxt("castro-sedov-scaling.txt")

for row in data:
    runs.append(ScalingRun(MPI=row[0], OMP=row[1], max_grid=row[4], 
                           nzones=row[5], max_level=row[6], time=row[7], std=row[8]))


sizes = set([int(q.nzones) for q in runs])
levels = [0, 1]#set([int(q.max_level) for q in runs])

markers = ["o", "^", "s"]

for nl in levels:
    for i, nz in enumerate(sizes):
        nz_runs = [q for q in runs if q.nzones == nz and q.max_level == nl]
        if len(nz_runs) == 0:
            continue

        c = [q.cores for q in nz_runs]
        t = [q.time for q in nz_runs]
        err = [q.std for q in nz_runs]

        color="C{:1d}".format(int(i % len(sizes)))
        plt.errorbar(c, t, yerr=err, fmt=markers[nl], color=color)
        plt.plot(c, trend_line(c, t), ls=":", color=color)

plt.xscale("log")
plt.yscale("log")

plt.ylim(1, 50)
plt.xlabel("number of cores")
plt.ylabel("avg. time / step")

# custom legend
legs = []
legnames = []

for i, nz in enumerate(sizes):
    color="C{:1d}".format(int(i % len(sizes)))
    legs.append(plt.Line2D((0,1),(0,0), color=color))
    legnames.append(r"${}^3$".format(nz))

plt.legend(legs, legnames, frameon=False,
           fontsize="small", numpoints=1, loc=3)


ax = plt.gca()
plt.text(0.95, 0.95, "Castro 3-d Sedov (pure hydro)", 
         fontsize="small", horizontalalignment="right", transform = ax.transAxes)


plt.tight_layout()

f = plt.gcf()
f.set_size_inches(8, 6)

plt.savefig("sedov_scaling.pdf", dpi=150, bbox_inches="tight")
