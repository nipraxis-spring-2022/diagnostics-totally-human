"""
This module defines functions implementing algorithms in SPM

Here you want the get_spm_globals function from the earlier
``four_dimensions_exercise``, with anything that function imports and other
definitions that the function needs.

See:
    https://bic-berkeley.github.io/psych-214-fall-2016/four_dimensions_exercise.html

In the same directory as this file, you will find a 'tests' directory.

Test this module with:

    python3 findoutlie/tests/test_spm_funcs.py

or better, in IPython::

    %run findoutlie/tests/test_spm_funcs.py
"""

# Any imports you need
import numpy as np
import nibabel as nib
import nipraxis


def spm_global(vol):
    """ Calculate SPM global metric for array `vol`

    Parameters
    ----------
    vol : array
        Array giving image data, usually 3D.

    Returns
    -------
    g : float
        SPM global metric for `vol`
    """
    T = np.mean(vol) / 8
    g = np.mean(vol[vol > T])
    return g

def get_spm_globals(fname):

    """ Calculate SPM global metrics for volumes in image filename `fname`

    Parameters
    ----------
    fname : str
        Filename of file containing 4D image

    Returns
    -------
    spm_vals : array
        SPM global metric for each 3D volume in the 4D image.
    """


    #print('fname being passed',fname)
    img = nib.load(fname)
    data = img.get_fdata()
    spm_vals = []
    for i in range(data.shape[-1]):
       vol = data[...,i]
       spm_vals.append(spm_global(vol))
    return spm_vals

def main(fname):
    # This function runs when file is executed as a script
   # bold_fname = nipraxis.fetch_file('ds107_sub012_t1r2.nii')
    glob_vals = get_spm_globals(fname)
    if glob_vals is None:
        raise ValueError('Did you return your global values ? ')
    expected_values = np.loadtxt('global_signals.txt')
    if np.allclose(glob_vals, expected_values, rtol=1e-4):
        print('OK: your values and PSMs are close')
    else:
        print('SPM and your values idiffer')
        print('Yours:', [float(v) for v in glob_vals])
        print('SPMs:', expected_values)

if __name__ == '__main__':
    # File being executed as a script
    main()

