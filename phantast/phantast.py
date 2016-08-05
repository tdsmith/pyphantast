import numpy as np
from scipy.ndimage.filters import gaussian_filter


def phantast(im, sigma, epsilon, halo_correction=False):
    if halo_correction:
        raise NotImplementedError("Halo correction is unimplemented")
    j = local_contrast(im, sigma, epsilon)
    return j


def local_contrast(im, sigma, epsilon):
    im = np.array(im, float)
    im /= im.max()
    imfilt = gaussian_filter(im, sigma)
    im2filt = gaussian_filter(im**2, sigma)
    contrast = np.sqrt((im2filt - imfilt**2) / imfilt)
    result = contrast < epsilon
    return result
