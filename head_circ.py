import nibabel as nib
import numpy as np
import os
import sys
import nipype
import nipype.interfaces.fsl
import shutil
import math

try: 


    # takes the input from the user and gets the abs path. 
    def setpath(argv):
        abs_path = os.path.abspath(os.path.join(os.getcwd(),argv))
        return abs_path

    path = setpath(sys.argv[1])
    #print(path)

    def copyfile():
        destination = (os.getcwd() + '/mask.nii.gz')
        print(path+" "+destination)
        shutil.copyfile(path, destination)
        return destination

    filename = sys.argv[1]
    maskname = filename.split('.')[0]+'_mask.nii.gz'
    outPathFile = os.path.join(os.getcwd(),maskname)

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
    print("\nxmax="+ str(xMax) + ", ymax=" + str(yMax) + " ,zmax=" + str(zMax))
    print("xDim="+ str(xDim) + ", ydim=" + str(yDim) + " ,zdim=" + str(zDim), end="\n\n")

    # get the cente voxel to work from. 
    center = input("Enter center voxel as 'x y z' seperated by a single space.\n")

    centerVoxel = center.split(' ')
    xCenter = int(centerVoxel[0])
    yCenter = int(centerVoxel[1])
    zCenter = int(centerVoxel[2])
    

    maskSize = int(input("\nEnter mask size\n"))
    xSpan = math.ceil(maskSize/xDim)
    xLower = xCenter
    ySpan = math.ceil(maskSize/yDim)
    zSpan = math.ceil(maskSize/zDim)

    zFactor = zDim/xDim


    newArray = np.zeros((xMax, yMax, zMax))

    for x in range(0, xMax):
        xdiff = xDim * abs(xCenter - x)
        for y in range(0, yMax):
            ydiff = yDim * abs(yCenter - y)
            for z in range(0, zMax):
                zdiff = zDim * abs(zCenter - z)
                if (math.sqrt(xdiff**2 + ydiff**2 + zdiff**2)) < maskSize:
                    newArray[x,y,z] = 1
    affine = np.diag([1, 1, 1, 1])
    arrayImg = nib.Nifti1Image(newArray, affine)
    nib.save(arrayImg, outPathFile)






except Exception as e: 
    print("Error occured, try again")
    print(e)

