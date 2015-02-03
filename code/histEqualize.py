# Outputs pdf and cdf of equalized histogram image
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

image = cv2.equalizeHist(image)

cv2.imwrite('equ_' + image_name, image)

hist = cv2.calcHist([image], [channel], None, [256], [0,256])

count = 0
for i in range(0,256):
	count += hist[i]

pdf = []
cdf = []
so_far = 0

for i in range(0,256):
	pdf.append(float(hist[i])/float(count))
	so_far += hist[i]
	cdf.append(float(so_far)/float(count))

plt.plot(pdf)
plt.savefig('pdf_equ_' + image_name)
plt.clf()

plt.plot(cdf)
plt.savefig('cdf_equ_' + image_name)
plt.clf()

#plt.plot(hist)
#plt.show()