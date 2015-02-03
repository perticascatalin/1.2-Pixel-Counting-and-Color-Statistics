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
	
	average = np.average(image)

	# Scale result to the interval [0,1] and print it
	print average/255.0
