import cv2
import sys
import numpy as np
from matplotlib import pyplot as plt

image_name = sys.argv[1]

img = cv2.imread(image_name, cv2.CV_LOAD_IMAGE_GRAYSCALE)
plt.hist(img.ravel(),256,[0,256])
#plt.show()
plt.savefig('hist_' + image_name)

#hist = cv2.calcHist([img], [0], None, [256], [0,256])
#plt.plot(hist)
#plt.show()