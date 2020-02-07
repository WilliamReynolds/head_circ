import nibabel as nib
import numpy as np
import os
import sys
import nipype
import nipype.interfaces.fsl
import shutil
import math
import matplotlib.pyplot as plt
import linecache
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

try: 
    path = setpath(sys.argv[1])
    filename = sys.argv[1]
    maskname = sys.argv[2]

    mri = nib.load(sys.argv[1]).get_fdata()
    mask = nib.load(sys.argv[2]).get_fdata()

    print(type(mri))    
    print(type(mask))    
    print(mri.shape)    
    print(mask.shape)

    print(np.average(mri))

    result = np.multiply(mri, mask)
    print(type(result))
    print(result.shape)
    print(np.average(result))
    avg = np.average(result)

    norm = np.divide(result, avg)
    print(type(norm))
    print(norm.shape)
    print(np.average(norm))
    norm[norm == 0] = 'nan'

    hist = np.histogram(norm, 100, density=False)
    print(hist)

    counts, bins = np.histogram(norm)
    plt.hist(bins[:-1], bins, weights=counts, density=True)
    plt.show()
    plt.clf()

except Exception as e: 
    print("Error occured, try again")
    print(e)
    print ('Error on line {}'.format(sys.exc_info()[-1].tb_lineno))


