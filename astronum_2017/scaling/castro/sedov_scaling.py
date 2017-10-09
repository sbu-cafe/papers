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
    trend = t[0]*c[0]/c[:]
    return trend

runs = []

data = np.loadtxt("castro-sedov-scaling.txt")

for row in data:
    runs.append(ScalingRun(MPI=row[0], OMP=row[1], max_grid=row[4], 
                           nzones=row[5], max_level=row[6], time=row[7], std=row[8]))


sizes = set([q.nzones for q in runs])

for nz in sizes:
    nz_runs = [q for q in runs if q.nzones == nz]
    c = [q.cores for q in nz_runs]
    t = [q.time for q in nz_runs]
    err = [q.std for q in nz_runs]

    color="C{:1d}".format(int(nz % len(sizes)))
    plt.errorbar(c, t, yerr=err, fmt="o", color=color)
    plt.plot(c, trend_line(c, t), ls=":", color=color)

plt.xscale("log")
plt.yscale("log")

plt.xlabel("cores")
plt.ylabel("avg. time / step")
plt.savefig("sedov_scaling.png")
