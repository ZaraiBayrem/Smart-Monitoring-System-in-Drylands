import sys
import numpy as np
import skimage.io
import skimage.filters
import requests
from datetime import time
import cv2

#response = requests.get("https://i.pinimg.com/originals/09/e7/0e/09e70e249650ae166b07b16d0bf8664d.jpg")
#file = open("test_image.png", "wb")
#file.write(response.content)
#file.close()

def density():
    filename="test_image.png"
# read the original image, converting to grayscale
    grayFrame = skimage.io.imread(fname=filename, as_gray=True)
#    grayFrame = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# blur before thresholding
    blur = skimage.filters.gaussian(grayFrame, sigma=1)
# perform adaptive thresholding to produce a binary image
    t = skimage.filters.threshold_otsu(blur)
    binary = blur > t
# save binary image; first find beginning of file extension
    dot = filename.index(".")
    binary_file_name = filename[:dot] + "-binary" + filename[dot:]
    skimage.io.imsave(fname=binary_file_name, arr=skimage.img_as_ubyte(binary))
# determine root mass ratio
    rootPixels = np.nonzero(binary)
    Pixels=[list(i) for i in rootPixels][0]

    w = binary.shape[1]
    h = binary.shape[0]

    density = len(Pixels) / (w * h)

# output in format suitable for .csv
    #print("Density= ",(1-density)*100," %")
    return density

