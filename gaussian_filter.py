import numpy as np
from utils import convolve

def gaussian_mask(size, sigma):
    ax = np.linspace(-(size - 1) / 2., (size - 1) / 2., size)
    xx, yy = np.meshgrid(ax, ax)
    kernel = np.exp(-0.5 * (np.square(xx) + np.square(yy)) / np.square(sigma))
    return kernel / np.sum(kernel)


def gaussian_fitler(image, size,sigma):
    return convolve(image, gaussian_mask(size, sigma))