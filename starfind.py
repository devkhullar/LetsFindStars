import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits
from astropy.modeling.models import Gaussian2D
from photutils.datasets import make_noise_image
from photutils.centroids import centroid_quadratic
from astropy.visualization import simple_norm 
from photutils.aperture import CircularAperture

def make_aperture_image():
    # create an artificial single source
    gmodel = Gaussian2D(42.1, 47.8, 52.4, 4.7, 4.7, 0)
    yy, xx = np.mgrid[0:100, 0:100]
    data = gmodel(xx, yy)
    bkg_sig = 2.4
    noise = make_noise_image(data.shape, mean=0., stddev=bkg_sig, seed=123)
    data += noise
    error = np.zeros_like(data) + bkg_sig

    # find the source centroid
    xycen = centroid_quadratic(data, xpeak=48, ypeak=52)
    xycen

    # define apertures
    aperture_radii = [i for i in range(1, 31)]
    apertures = [CircularAperture(xycen, r=r) for r in aperture_radii]

    norm = simple_norm(data, 'sqrt')
    fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(10, 10))
    ax1.imshow(data, norm=norm, origin='lower')
    apertures[5].plot(ax=ax1, color='C0', lw=2)
    apertures[10].plot(ax=ax1, color='C1', lw=2)
    apertures[15].plot(ax=ax1, color='C3', lw=2)
    apertures[24].plot(ax=ax1, color='C4', lw=2)

    for i in aperture_radii[:-1]:
        plt.imshow(data, norm=norm, origin='lower')
        apertures[i].plot(ax=ax2, color=f'C{i}', lw=1.5)
    plt.show()

if __name__ == '__main__':
    image = fits.getdata('M74.fits')
    plt.imshow(image, vmax=7, origin='lower',
               interpolation='nearest')
    plt.show()