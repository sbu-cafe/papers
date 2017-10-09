import numpy as np
import matplotlib.pyplot as plt

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
    cnew = np.array(list(set(c)))
    print(cnew)
    trend = t[0]*c[0]/cnew[:]
    return cnew, trend

runs = []

data = np.loadtxt("castro-wdmerger-scaling.txt")

for row in data:
    runs.append(ScalingRun(MPI=row[0], OMP=row[1], max_grid=row[4], 
                           nzones=row[5], max_level=row[6], time=row[7], std=row[8]))


sizes = set([q.nzones for q in runs])
#sizes = [512]
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

        color="C{:1d}".format(int(i % len(levels)))
        print(color, nz)
        plt.errorbar(c, t, yerr=err, fmt=markers[nl], color=color)
        ctrend, trend = trend_line(c, t)
        plt.plot(ctrend, trend, ls=":", color=color)

plt.xscale("log")
plt.yscale("log")

plt.xlabel("cores")
plt.ylabel("avg. time / step")
plt.savefig("wdmerger_scaling.pdf", dpi=150, bbox_inches="tight")
