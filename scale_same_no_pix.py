# Scales the provided images to the same number of pixels
# Each image should have about the same number of pixels as the one with the fewest pixels
# Run: python scale_same_no_pix.py <image_name1> <image_name2> ...
# Obtained images saved under: '0.jpg', '1.jpg', ...

import cv2
import sys
import math

no_images = len(sys.argv) - 1
image_name = []

for i in range(no_images):
	cur_name = sys.argv[i+1]
	image_name.append(cur_name)

image = []

for i in range(no_images):
	cur_image = cv2.imread(image_name[i])
	image.append(cur_image)

min_no_pix = image[0].shape[0] * image[0].shape[1]

for i in range(no_images):
	no_rows = image[i].shape[0]
	no_cols = image[i].shape[1]
	min_no_pix = min(min_no_pix, no_rows * no_cols) 

for i in range(no_images):
	no_rows = image[i].shape[0]
	no_cols = image[i].shape[1]
	ratio = math.sqrt((float(no_rows)*float(no_cols))/float(min_no_pix))
	n_rows = int(float(no_rows)/ratio)
	n_cols = int(float(no_cols)/ratio)
	image[i] = cv2.resize(image[i], (n_cols, n_rows))
	cv2.imwrite(str(i) + '.jpg', image[i])