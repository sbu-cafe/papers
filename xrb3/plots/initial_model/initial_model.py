import matplotlib.pyplot as plt
import numpy as np


def initial_model():

    cool_model = "flame_wave_new_cool.out"
    hot_model = "flame_wave_new_hot.out"

    cool_data = np.loadtxt(cool_model)
    hot_data = np.loadtxt(hot_model)


    # make the plots
    r_min = 0
    r_max = 10000.0

    r_min = 0
    r_max = 4500

    #-------------------------------------------------------------------------
    # density and temperature plots
    #-------------------------------------------------------------------------
    dens_min = 1.e2
    dens_max = 5.e8

    sp = plt.subplot(121)

    sp.set_yscale('log')


    # density
    plt.plot(cool_data[:,0], cool_data[:,1], color="C0")
    plt.plot(hot_data[:,0], hot_data[:,1], color="C0", ls="--")

    plt.xlabel(r"z (cm)")
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
    #plt.axis(color="C1")
    plt.ylabel(r"temperature (K)", color="C1")

    plt.xlabel(r"z (cm)")

    plt.xlim(r_min, r_max)
    plt.ylim(8.e6, 2.e9)

    #-------------------------------------------------------------------------
    # species
    #-------------------------------------------------------------------------

    sp = plt.subplot(122)

    sp.set_yscale('log')

    plt.plot(cool_data[:,0], cool_data[:,3], color="C0", label="$X({}^4\mathrm{He})$")
    plt.plot(hot_data[:,0], hot_data[:,3], color="C0", ls="--")

    plt.plot(cool_data[:,0], cool_data[:,4], color="C1", label="$X({}^{56}\mathrm{Ni})$")
    plt.plot(hot_data[:,0], hot_data[:,4], color="C1", ls="--")

    plt.xlabel(r"z (cm)")
    plt.ylabel(r"mass fraction")

    plt.xlim(r_min, r_max)
    plt.ylim(1.e-2, 1.1)

    plt.legend()

    #-------------------------------------------------------------------------
    #plt.subplots_adjust(hspace=0.1)

    f = plt.gcf()
    f.set_size_inches(10.0,6.0)

    f.tight_layout()

    plt.savefig("initial_model_paper.pdf", bbox_inches='tight')

if __name__== "__main__":
    initial_model()

