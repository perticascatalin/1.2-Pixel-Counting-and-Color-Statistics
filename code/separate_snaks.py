import cv2
import numpy as np
import sys

no_images = len(sys.argv) - 1
image_names = []

for i in range(no_images):
	image_names.append(sys.argv[i+1])

images = []

for i in range(no_images):
	image = cv2.imread(image_names[i], 0)
	ret, image = cv2.threshold(image, 100, 255, cv2.THRESH_BINARY)
	cv2.imwrite('result.png', image)
	images.append(image)