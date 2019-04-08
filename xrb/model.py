import numpy as np
import matplotlib.pyplot as plt

z_max = 10
z = np.linspace(0, z_max, 200)

H_star = 4
delta_atm = 1
z_isentropic = 3

T_star = 1.0
T_hi = 2.0
T_lo = 1.2

T = T_star*np.ones_like(z)

idx = z > H_star
T[idx] = (T_hi - T_star)/delta_atm*(z[idx] - H_star)  + T_star

plt.plot([H_star, H_star], [0.9, 2.1], color="C0", ls=":")
plt.text(H_star/2, 1.8, "star layer", color="C0", horizontalalignment="center", fontsize="small")

plt.text(-0.1, T_star, r"$T_\star$", horizontalalignment="right")

idx = z > H_star + delta_atm
T[idx] = (T_lo - T_hi)/z_isentropic*(z[idx] - (H_star + delta_atm)) + T_hi

plt.plot([H_star + delta_atm, H_star + delta_atm], [0.9, 2.1], color="C0", ls=":")
plt.text(H_star+delta_atm/2, 1.8, "ramp\nlayer", color="C0", horizontalalignment="center", fontsize="small")
plt.plot([0, H_star + delta_atm], [T_hi, T_hi], color="0.5", ls=":")
plt.text(-0.1, T_hi, r"$T_\mathrm{hi}$", horizontalalignment="right")

T[z > H_star + delta_atm + z_isentropic] = T_lo

plt.plot([H_star + delta_atm + z_isentropic, H_star + delta_atm + z_isentropic], [0.9, 2.1], color="C0", ls=":")
plt.text(H_star+delta_atm + z_isentropic/2, 1.8, "fuel\nlayer", color="C0", horizontalalignment="center", fontsize="small")

plt.plot([0, H_star + delta_atm + z_isentropic], [T_lo, T_lo], color="0.5", ls=":")
plt.text(-0.1, T_lo, r"$T_\mathrm{lo}$", horizontalalignment="right")


plt.text(H_star+delta_atm + z_isentropic + 0.5*(z_max - (H_star+delta_atm+z_isentropic)),
         1.8, "outer\nbuffer", color="C0", horizontalalignment="center", fontsize="small")
plt.plot(z, T, color="C1")
plt.axis("off")

plt.plot([0, 11], [0.9, 0.9], color="k")
plt.text(11, 0.9, r"$y$", color="k", verticalalignment="top")

plt.plot([0, 0], [0.9, 2.1], color="k")
plt.text(-0.1, 2.1, r"$T(y)$", color="k", horizontalalignment="right")

plt.plot([H_star, H_star], [0.9-0.025, 0.9+0.025], color="k")
plt.text(H_star, 0.9-0.03, r"$H_\star$", horizontalalignment="center", verticalalignment="top")

plt.tight_layout()

f = plt.gcf()
f.set_size_inches(6.0,6.0)

plt.savefig("model.pdf", bbox_inches="tight", pad_inches=0.0)


