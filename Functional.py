import nibabel as nib
import numpy as np
import os
import sys
import nipype
import nipype.interfaces.fsl
import shutil
import math
'''
1. get both functional file and mask file
2. for xyzt in functional, check mask 
    -0 then set to nan
3. calculate avg over t dimension
4. singular subject, need to create module/function to apply to batches
5. Output results to histograms and compare distirbutions

'''

# takes the input from the user and gets the abs path. 
def setpath(argv):
    abs_path = os.path.abspath(os.path.join(os.getcwd(),argv))
    return abs_path

def copyfile():
    destination = (os.getcwd() + '/mask.nii.gz')
    print(path+" "+destination)
    shutil.copyfile(path, destination)
    return destination

def MinMax(minMax, center, span, sign):
    if (sign == '+'):
        if (center + span) >= minMax:
            return minMax
        else:
            return center + span
    if (sign == '-'):
        if (center - span <= minMax):
            return minMax
        else:
            return center - span

try: 
    path = setpath(sys.argv[1])
    filename = sys.argv[1]
    maskname = sys.argv[2]
    #outPathFile = os.path.join(os.getcwd(),maskname)

    # gets the image header info 
    img = nib.load(sys.argv[1])
    pixDim = (img.header['pixdim'])
    dimensions = img.header.get_data_shape()
    xDim = np.around(pixDim[1],2)
    xMax = (dimensions[0])
    yDim = np.around(pixDim[2],2)
    yMax = (dimensions[1])
    zDim = np.around(pixDim[3],2)
    zMax = (dimensions[2])
    tDim = np.around(pixDim[4],2)
    tMax = (dimensions[3])
    print("\nxmax="+ str(xMax) + ", ymax=" + str(yMax) + " ,zmax=" + str(zMax))
    print("xDim="+ str(xDim) + ", ydim=" + str(yDim) + " ,zdim=" + str(zDim), end="\n\n")

    




except Exception as e: 
    print("Error occured, try again")
    print(e)

