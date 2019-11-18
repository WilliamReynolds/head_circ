import nibabel as nib
import numpy as np
import os
import sys
import nipype
import nipype.interfaces.fsl
import shutil

try: 


    # takes the input from the user and gets the abs path. 
    def setpath(argv):
        abs_path = os.path.abspath(os.path.join(os.getcwd(),argv))
        return abs_path

    path = setpath(sys.argv[1])

    def copyfile():
        destination = (os.getcwd() + '/mask.nii.gz')
        print(path+" "+destination)
        shutil.copyfile(path, destination)
        return destination
    
    destination = copyfile()

    def getCenterVoxel():
        center = input("Enter center voxel.\n")
        return center

    center = getCenterVoxel()

    # gets the image header info 
    img = nib.load(sys.argv[1])
    data = img.get_data()
    pixdim = (img.header['pixdim'])
    dimensions = img.header.get_data_shape()
    xdim = np.around(pixdim[1],2)
    xmax = (dimensions[0])
    ydim = np.around(pixdim[2],2)
    ymax = (dimensions[1])
    zdim = np.around(pixdim[3],2)
    zmax = (dimensions[2])
    print("xmax="+ str(xmax) + ", ymax=" + str(ymax) + " ,zmax=" + str(zmax))
    print("xdim="+ str(xdim) + ", ydim=" + str(ydim) + " ,zdim=" + str(zdim))
    #print (xdim)
    #print (ydim)
    #print (zdim)
    

    mask_img = nib.load(destination)
    print(nib.is_proxy(mask_img))
    print(type(mask_img))
    temp = input("enter to continue")
    xcount = 0

    while xcount <= xmax:
        ycount = 0
        while ycount <= ymax:
            zcount = 0
            while zcount <= zmax:
                print(xcount + ycount + zcount)
                zcount += 1
            ycount += 1
        xcount += 1


except Exception as e: 
    print("Error occured, try again")
    print(e)

