import matplotlib.pyplot as plt
import random
import matplotlib as mpl
from matplotlib import cm

class Box(object):

    def __init__(self, ll, uu, nx, ny, grid_color="0.5", ng=0):

        self.ll = ll
        self.uu = uu
        self.nx = nx
        self.ny = ny
        self.grid_color = grid_color
        self.ng = ng

        self.dx = (self.uu[0] - self.ll[0])/self.nx
        self.dy = (self.uu[1] - self.ll[1])/self.ny

    def draw(self):

        # draw the frame
        plt.plot([self.ll[0], self.ll[0], self.uu[0], self.uu[0], self.ll[0]],
                 [self.ll[1], self.uu[1], self.uu[1], self.ll[1], self.ll[1]],
                 color=self.grid_color, lw=2)

        # draw the x grid lines
        for n in range(1, self.nx):
            plt.plot([self.ll[0] + n*self.dx, self.ll[0] + n*self.dx],
                     [self.ll[1], self.uu[1]],
                     color=self.grid_color, ls=":", lw=1)

        # draw the y grid lines
        for n in range(1, self.ny):
            plt.plot([self.ll[0], self.uu[0]],
                     [self.ll[1] + n*self.dy, self.ll[1] + n*self.dy],
                     color=self.grid_color, ls=":", lw=1)

        # ghostcells?
        if self.ng > 0:
            xmin = self.ll[0] - self.ng*self.dx
            xmax = self.uu[0] + self.ng*self.dx
            ymin = self.ll[1] - self.ng*self.dy
            ymax = self.uu[1] + self.ng*self.dy

            plt.plot([xmin, xmin, xmax, xmax, xmin],
                     [ymin, ymax, ymax, ymin, ymin],
                     ls="--", color="r")


    def tile(self, num_x):

        tile_nx = int(self.nx / num_x)
        if self.nx % num_x != 0:
            tile_nx += 1

        for n in range(num_x):
            xl = self.ll[0] + n*tile_nx*self.dx
            xr = min(self.ll[0] + (n+1)*tile_nx*self.dx, self.uu[0])

            plt.fill([xl, xl, xr, xr, xl],
                     [self.ll[1], self.uu[1], self.uu[1], self.ll[1], self.ll[1]],
                     color="C{}".format(n), alpha=0.5)


    def gpu_color(self):
        """every grid cell is a different color"""

        norm = mpl.colors.Normalize(vmin=0, vmax=self.nx*self.ny)

        i = 0
        for n in range(self.nx):
            xl = self.ll[0] + n*self.dx
            xr = self.ll[0] + (n+1)*self.dx

            for m in range(self.ny):
                yl = self.ll[1] + m*self.dy
                yr = self.ll[1] + (m+1)*self.dy

                #plt.fill([xl, xl, xr, xr, xl],
                #         [yl, yr, yr, yl, yl],
                #         color="C{}".format(random.randrange(0,7)), alpha=random.choice([0.2, 0.4, 0.6, 0.8]))

                plt.fill([xl, xl, xr, xr, xl],
                         [yl, yr, yr, yl, yl],
                         color=cm.viridis(norm(i)), alpha=(0.2 * (i % 5) + 0.2)) #ndrange(0,7)), alpha=random.choice([0.2, 0.4, 0.6, 0.8]))

                i += 1

    def label(self, ix, iy, offx, offy, text):
        xx = self.ll[0] + (ix + 0.5)*self.dx
        yy = self.ll[1] + (iy + 0.5)*self.dy
        plt.annotate(text, xy=(xx, yy),
                     xytext=(xx + offx*self.dx, yy + offy*self.dy),
                     arrowprops=dict(facecolor='black', shrink=0.05, lw=1))

def clean_and_save(outfile):

    ax = plt.gca()
    ax.set_aspect("equal") #, "datalim")
    plt.axis("off")

    f = plt.gcf()
    f.set_size_inches(7.0, 5.25)

    ax.set_xlim(-0.25, 2.75)
    ax.set_ylim(-0.25, 1.75)

    plt.savefig(outfile, bbox_inches="tight")


box_info = [[(0., 0.), (1., 1.), (5, 5)],
            [(1., 0.4), (2.2, 1.4), (6, 5)]]

boxes = []

plt.clf()

for lo, hi, ncell in box_info:
    boxes.append(Box(lo, hi, ncell[0], ncell[1]))
    boxes[-1].draw()

boxes[-1].label(0, 0, 3, -2, r"$\mathtt{lo(:)}$")
boxes[-1].label(boxes[-1].nx-1, boxes[-1].ny-1, 1, 2, r"$\mathtt{hi(:)}$")

#plt.xlim(-0.25,3.25)
#plt.ylim(-0.25,2.25)


clean_and_save("gpu_1.pdf")


# OpenMP fig

plt.clf()

for bx in boxes:
    bx.draw()

boxes[-1].tile(2)

boxes[-1].label(0, 0, 3, -2, r"$\mathtt{lo}_\mathrm{tile}\mathtt{(:)}$")
boxes[-1].label(2, 4, 1, 2, r"$\mathtt{hi}_\mathrm{tile}\mathtt{(:)}$")
clean_and_save("gpu_2.pdf")


# GPU figure

plt.clf()

for bx in boxes:
    bx.draw()

boxes[-1].gpu_color()

boxes[-1].label(0, 0, 3, -2, r"$\mathtt{lo}_\mathrm{gpu}\mathtt{(:)} = \mathtt{hi}_\mathrm{gpu}\mathtt{(:)}$")

clean_and_save("gpu_3.pdf")



