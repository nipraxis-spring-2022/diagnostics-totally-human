""" Scan outlier metrics
"""

import numpy as np


def dvars(img):
    """ Calculate dvars metric on Nibabel image `img`

    The dvars calculation between two volumes is defined as the square root of
    (the sum of the (voxel differences squared) divided by the number of
    voxels).

    Parameters
    ----------
    img : nibabel image

    Returns
    -------
    dvals : 1D array
        One-dimensional array with n-1 elements, where n is the number of
        volumnes in `img`.
    """
    data = img.get_fdata()
    n_trs = data.shape[-1]
    n_voxels = np.prod(data.shape[:-1])

    data_reshaped = np.reshape(data, (n_voxels, n_trs))
    diff = np.diff(a = data_reshaped, n = 1, axis=1)
    dvals = np.sqrt(np.sum(diff ** 2, axis=0) / n_voxels)

    return dvals