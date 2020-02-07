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
    data = nb.load(filename)
    maskname = filename.split('.')[0]+'_bmask.nii.gz'
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

    maskSize = int(input("\nEnter mask size\n"))
    #get the span for region
    xSpan = math.ceil(maskSize/xDim)
    ySpan = math.ceil(maskSize/yDim)
    zSpan = math.ceil(maskSize/zDim)
    
    # set upper and lower bounds
    xUpper = MinMax(xMax, xCenter, xSpan, '+')
    xLower = MinMax(0, xCenter, xSpan, '-')
    yUpper = MinMax(yMax, yCenter, ySpan, '+')
    yLower = MinMax(0, yCenter, ySpan, '-')
    zUpper = MinMax(zMax, zCenter, zSpan, '+')
    zLower = MinMax(0, zCenter, zSpan, '-')



    zFactor = zDim/xDim


    newArray = np.zeros((xMax, yMax, zMax))

    for x in range(xLower, xUpper):
        xdiff = xDim * abs(xCenter - x)
        for y in range(yLower, yUpper):
            ydiff = yDim * abs(yCenter - y)
            for z in range(zLower, zUpper):
                zdiff = zDim * abs(zCenter - z)
                if (math.sqrt(xdiff**2 + ydiff**2 + zdiff**2)) < maskSize:
                    newArray[x,y,z] = 1
    affine = np.diag([1, 1, 1, 1])
    arrayImg = nib.Nifti1Image(newArray, affine)
    nib.save(arrayImg, outPathFile)






except Exception as e: 
    print("Error occured, try again")
    print(e)

