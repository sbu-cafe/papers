import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({'xtick.labelsize': 14,
                     'ytick.labelsize': 14,
                     'font.size': 14})

plt.rc("axes", linewidth=1.5)
plt.rc("lines", markeredgewidth=1.5)

class ScalingRun(object):
    def __init__(self, MPI=1, OMP=1, max_grid=1, nzones=1, nodes=1, max_level=1, time=0.0, std=0.0, compiler=""):
        self.MPI = MPI
        self.OMP = OMP
        self.nodes = nodes
        self.cores = MPI * OMP
        self.max_grid = max_grid
        self.nzones = nzones
        self.max_level = max_level
        self.time = time
        self.compiler = compiler
       # self.std = std


def trend_line(c, t):
    cnew = np.array(sorted(list(set(c))))
    print(cnew)
    trend = t[0]*c[0]/cnew[:]
    return cnew, trend

runs = []

data = np.loadtxt("castro-wdmerger-scaling.txt")


for row in data:
    runs.append(ScalingRun(MPI=row[0], OMP=row[1], nodes=row[3], max_grid=row[4], 
                           nzones=row[5], max_level=row[6], time=row[7], compiler=row[8]))


sizes = set([int(q.nzones) for q in runs])
#sizes = [512]
levels = [0, 1]#set([int(q.max_level) for q in runs])

markers = ["o", "^", "s"]
gnu_colors = ["C0", "C1"]
intel_colors = ["C9", "C3"]

compiler = {0: "gnu", 1: "intel"}

for comp in compiler:
    for nl in levels:
        for i, nz in enumerate(sizes):
            nz_runs = [q for q in runs if q.nzones == nz and q.max_level == nl and q.compiler == comp]
            if len(nz_runs) == 0:
                continue

            n = [q.nodes for q in nz_runs]
            t = [q.time for q in nz_runs]

            if compiler[comp] == "gnu":
                color = gnu_colors[int(i % len(levels))]
            elif compiler[comp] == "intel":
                color = intel_colors[int(i % len(levels))]

            print(color, nz)
            plt.scatter(n, t, c=color, marker=markers[nl])
            #plt.errorbar(n, t, yerr=err, fmt=markers[nl], color=color)
            ntrend, trend = trend_line(n, t)
            plt.plot(ntrend, trend, ls=":", color=color)

plt.xscale("log")
plt.yscale("log")

plt.ylim(0., 200.)

plt.xlabel("number of nodes")
plt.ylabel("avg. time / step")

threads_per_node = 68*4
ax = plt.gca()
ax.set_xlim(4, 256)

ax2 = ax.twiny()
ax2.set_xlim(4*threads_per_node, 256*threads_per_node)
ax2.set_xlabel("number of threads")

plt.ylim(0.5, 100)

# custom legend
legs = []
legnames = []

for i, nz in enumerate(sizes):
    for c in compiler:

        if compiler[c] == "gnu":
            color = gnu_colors[int(i % len(sizes))]
        elif compiler[c] == "intel":
            color = intel_colors[int(i % len(sizes))]

        legs.append(plt.Line2D((0,1),(0,0), color=color))
        legnames.append(r"${}^3$ {}".format(nz, compiler[c]))

legs.append(plt.Line2D((0,1),(0,0), color="k",
                       marker="o", markeredgecolor="k", markerfacecolor="k", linestyle="none"))
legnames.append("no AMR")

legs.append(plt.Line2D((0,1),(0,0), color="k",
                       marker="^", markeredgecolor="k", markerfacecolor="k",  linestyle="none"))
legnames.append("base + one 4x level")

plt.legend(legs, legnames, frameon=False,
           fontsize="11", numpoints=1, loc=3, ncol=3)

ax = plt.gca()
plt.text(0.95, 0.95, "Castro 3-d wdmerger (hydro + Poisson gravity)", 
         fontsize="small", horizontalalignment="right", transform = ax.transAxes)

plt.tight_layout()

f = plt.gcf()
f.set_size_inches(8, 6)

plt.savefig("cori_scaling.pdf", dpi=150, bbox_inches="tight")
