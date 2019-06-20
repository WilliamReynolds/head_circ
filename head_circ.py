"""
to input center voxel and then make mask based on circumference.


Gereral flow

import img > numpy
get voxel dimensions
get center voxel
find best estimate for head circ
make new array of same size of 0

for ijk in array do
if sizedistance < circ: 
    1
    else
    0

make nibabl image from numpy array
output file


"""

import nibabel as nib
import numpy as np
import os
import sys
import nipype
import nipype.interfaces.fsl
import shutil

# takes the input from the user and gets the abs path. 
def setpath(argv):
    abs_path = os.path.abspath(os.path.join(os.getcwd(),argv))
    return abs_path

path = setpath(sys.argv[1])
print (path)

# gets the image header info 
def imagetoarray(img):
    img = nib.load(sys.argv[1])
    data = img.get_data()
    #print(img.shape)
    #print (data.shape)
    #print(type(data))
    #print (img.header)
    pixdim = (img.header['pixdim'])
    xdim = np.around(pixdim[1],2)
    ydim = np.around(pixdim[2],2)
    zdim = np.around(pixdim[3],2)
    #print(type(xdim))
    print (xdim)
    print (ydim)
    print (zdim)
    

imagetoarray(path)

def copyimage(img):
    newfile = os.path.abspath(os.path.join(os.getcwd(),"mask.nii.gz"))
    shutil.copyfile(path,newfile)
    threshold = nipype.interfaces.fsl.Threshold()
    threshold.thresh(100)
    threshold.in_file(newfile)
    threshold.run()
copyimage(path)
