import numpy as np
import matplotlib.pyplot as plt

def initial_model():

    cool_model = "flame_wave_new_cool.out"
    hot_model = "flame_wave_new_hot.out"

    cool_data = np.loadtxt(cool_model)
    hot_data = np.loadtxt(hot_model)


    # make the plots
    r_min = 0
    r_max = 10000.0

    r_min = 4500
    r_max = 7000

    #-------------------------------------------------------------------------
    # density and temperature plots
    #-------------------------------------------------------------------------
    dens_min = 1.e2
    dens_max = 5.e8

    sp = plt.subplot(111)

    sp.set_yscale('log')


    # density
    plt.plot(cool_data[:,0], cool_data[:,1], color="C0")
    plt.plot(hot_data[:,0], hot_data[:,1], color="C0", ls="--")

    plt.xlabel(r"y (cm)")
    plt.ylabel(r"density (g cm$^{-3}$)", color="C0")

    plt.xlim(r_min, r_max)
    plt.ylim(dens_min, dens_max)

    ax = plt.gca()

    # the offset text is the 1.e8 that appears under the axis labels when
    # doing scientific notation
    #ax.tick_params(labeltop='off')
    #ax.tick_params(labelbottom='off')
    ax.xaxis.offsetText.set_visible(False)

    # temperature
    sp2 = plt.twinx()
    sp2.set_yscale('log')

    # original
    plt.plot(cool_data[:,0], cool_data[:,2], color="C1")
    plt.plot(hot_data[:,0], hot_data[:,2], color="C1", ls="--")

    sp2.yaxis.tick_right()
    plt.axis(labelcolor="C1")
    plt.ylabel(r"temperature (K)", color="C1")

    plt.xlabel(r"y (cm)")

    plt.xlim(r_min, r_max)
    plt.ylim(8.e6, 2.e9)


    #-------------------------------------------------------------------------
    #plt.subplots_adjust(hspace=0.1)

    f = plt.gcf()
    f.set_size_inches(6.0,6.0)

    f.tight_layout()

    plt.savefig("initial_model_paper.pdf", bbox_inches='tight')

if __name__== "__main__":
    initial_model()

