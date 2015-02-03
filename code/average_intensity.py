# Extracts the average intensity for a number of images
# The result is scaled to the interval [0,1]
# Run: python average_intensity.py <image_name_0> <image_name_1> ...

import cv2
import sys
import numpy as np

# Get the number of images in the input
no_images = len(sys.argv) - 1

# Fetch all image names
image_name = []
for i in range(no_images):
	image_name.append(sys.argv[i+1])

# Iterate through all images
for i in range(no_images):
	image = cv2.imread(image_name[i], 0)
	no_rows = image.shape[0]
	no_cols = image.shape[1]
	sumall = 0.0
	# Iterate through all pixels and compute the sum of their intensities
	for row in range(no_rows):
		for col in range(no_cols):
			sumall += float(image[row, col])
	average = sumall/float(no_rows*no_cols)

	# Scale result to the interval [0,1] and print it
	print average/255.0
