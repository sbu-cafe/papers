import numpy as np
import matplotlib.pyplot as plt

# read the Strang data into a numpy array
strang = np.loadtxt("strang_diag.out")

# now manually read it looking for the times that indicate when the Strang halves began
strang_starts = []
strang_second = []
with open("strang_diag.out") as f:
    for line in f:
        if line.startswith(" # start of step"):
            _, time = line.split("=")
            strang_starts.append(float(time))
        elif line.startswith(" # second half of strang"):
            _, time = line.split("=")
            strang_second.append(float(time))

strang_starts = sorted(set(strang_starts))
strang_second = sorted(set(strang_second))

print(strang_starts)

# now get the SDC data
sdc = np.loadtxt("sdc_diag.out")

# we have 2 SDC iterations here, so be able to separate them
idx_iter0 = sdc[:,1] == 0
idx_iter1 = sdc[:,1] == 1


# make the plots
plt.scatter(strang[:,0], strang[:,2], marker="x", s=15, label="Strang splitting")
plt.scatter(sdc[idx_iter1,0], sdc[idx_iter1,3], marker="o", s=15, label="SDC")

# draw timestep boundaries
for time in strang_starts:
    plt.plot([time, time], [0,1], color="k", linewidth=2)

for time in strang_second:
    plt.plot([time, time], [0,1], color="0.5", linestyle=":", linewidth=2)

plt.xlim(1.8685965733085516e-05,1.8999075234060896e-05)
plt.ylim(0.5872, 0.5884)

plt.legend(frameon=False)

plt.tight_layout()

f = plt.gcf()
f.set_size_inches(9.0, 7.0)

plt.xlabel("time (s)", fontsize="large")
plt.ylabel(r"$X({}^4\mathrm{He})$", fontsize="large")

plt.savefig("sdc_plot.png")

print("sdc points = ", len(sdc[idx_iter1,0]))
print("strang points = ", len(strang[:,0]))
