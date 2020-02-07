from nipy import load_image, save_image
import numpy as np
#import getpass
from nipy.core.api import Image, vox2mni
import os
import sys


"""
Takes as input the file path to a nifti (.nii) 
and returns a numpy array
"""


def load_nii(nii):
    """
    Returns the image data and the coordinate space from the header
    The coordinate space is useful for saving the image back in the 
    same 3D space as the original
    """
    img = load_image(nii)
    data = img.get_data()
    coord = img.coordmap
    return data, coord


def save_nii(data, coord, save_file):
    """
    Saves a numpy array (data) as a nifti file
    The coordinate space must match the array dimensions
    """
    arr_img = Image(data, coord)
    save_image(arr_img, save_file)
    return 0


if __name__ == '__main__':

    input_image = os.path.abspath(sys.argv[1])
    numpy_array = load_nii(input_image)
    print(numpy_array.shape)
