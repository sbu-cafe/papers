import matplotlib
import matplotlib.pyplot as plt
import numpy as np

matplotlib.rc('text', usetex=True) 
matplotlib.rcParams.update({"font.size": 18})
matplotlib.rcParams['text.latex.preamble']=r"""
\usepackage{amsmath}
\newcommand{\pluseq}{\mathrel{+}=}"""

# first strang

fig = plt.figure()
ax = fig.add_subplot(111)
ax.axis("off")


dy = 1.0
dx = 1.0

eps = 0.075

# top line

y = 2*dy

ax.arrow(0, y, dx, 0, head_width=0.075, length_includes_head=True,
         linewidth=2.0, color="C0")

ax.text(0-eps, y, r"$\boldsymbol{\mathcal{U}}^n$", verticalalignment="center", horizontalalignment="right", color="C0")
ax.text(dx+eps, y, r"$\boldsymbol{\mathcal{U}}^\star$", verticalalignment="center", horizontalalignment="left", color="C0")

ax.text(dx/2, y+eps, r"$\frac{d\boldsymbol{\mathcal{U}}}{dt} = {\bf R}$", verticalalignment="bottom", horizontalalignment="center", color="C0")

# middle line

y = dy

ax.arrow(0, y, 2*dx, 0, head_width=0.075, length_includes_head=True, linewidth=2.0, color="C1")

ax.text(0-eps, y, r"$\boldsymbol{\mathcal{U}}^\star$", verticalalignment="center", horizontalalignment="right", color="C1")
ax.text(2*dx+eps, y, r"$\boldsymbol{\mathcal{U}}^{n+1,\star}$", verticalalignment="center", horizontalalignment="left", color="C1")

ax.text(dx, y+eps, r"$\boldsymbol{\mathcal{U}^\star} \pluseq \boldsymbol{\mathcal{A}}(\boldsymbol{\mathcal{U}^{\star,n+1/2}})$", verticalalignment="bottom", horizontalalignment="center", color="C1")

# bottom line

y = 0

ax.arrow(dx, y, dx, 0, head_width=0.075, length_includes_head=True, linewidth=2.0, color="C0")

ax.text(dx-eps, y, r"$\boldsymbol{\mathcal{U}}^{n+1,\star}$", verticalalignment="center", horizontalalignment="right", color="C0")
ax.text(2*dx+eps, y, r"$\boldsymbol{\mathcal{U}}^{n+1}$", verticalalignment="center", horizontalalignment="left", color="C0")

ax.text(3*dx/2, y+eps, r"$\frac{d\boldsymbol{\mathcal{U}}}{dt} = {\bf R}$", verticalalignment="bottom", horizontalalignment="center", color="C0")


# draw time

ax.vlines(0, -0.5*dy, 2.5*dy, linestyle=":", color="0.5")
ax.vlines(2 * dx, -0.5*dy, 2.5*dy, linestyle=":", color="0.5")

ax.text(0, -0.5*dy-eps, r"$t^n$", color="0.5", verticalalignment="top", horizontalalignment="center")
ax.text(2*dx, -0.5*dy-eps, r"$t^{n+1}$", color="0.5", verticalalignment="top", horizontalalignment="center")

fig.set_size_inches(8.0, 3.5)
fig.savefig("sdc_strang_flowchart.pdf", dpi=200)
