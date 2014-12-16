# Concatenates images horizontally
# All images are resized to have the number of rows equal the minimum among all images

import cv2
import sys
import numpy as np

borderLen = sys.argv[1]
no_images = len(sys.argv) - 2
image_name = []
for i in range(no_images):
	image_name.append(sys.argv[i+2])
image = []
for i in range(no_images):
	cur_image = cv2.imread(image_name[i])
	image.append(cur_image)
