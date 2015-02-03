# Outputs histogram of given image
# Arguments: image_name, 0 for grayscale and 1 for BGR, if BGR image which channel(0,1 or 2)

import cv2
import sys
import numpy as np
from matplotlib import pyplot as plt


image_name = sys.argv[1]
gsvsrgb = int(sys.argv[2])
channel = 0
if gsvsrgb == 1:
	channel = int(sys.argv[3])

image = cv2.imread(image_name, gsvsrgb)
no_rows = image.shape[0]
no_cols = image.shape[1]
total_pixels = no_rows * no_cols

hist = cv2.calcHist([image], [channel], None, [256], [0,256])

count = 0
for i in range(100,256):
	count += hist[i]

print int(count)
print float(count)/total_pixels

plt.plot(hist)
plt.savefig('hist_' + image_name)

#max_col = (0,0,0)
#max_no_pix = 0.0
#for blue in range(256):
#	for green in range(256):
#		for red in range(256):
#			if max_no_pix < hist[blue, green, red]:
#				max_no_pix = hist[blue, green, red]
#				max_col = (blue, green, red)

#print max_col, max_no_pix

#plt.plot(hist)
#plt.show()