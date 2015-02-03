# Run: python concatenate_images_vertically.py <border_length> <image_name_1> <image_name_2> ...
# Concatenates images vertically
# All images are resized to have the number of columns equal the minimum among all images

import cv2
import sys
import numpy as np

border_len = int(sys.argv[1])
no_images = len(sys.argv) - 2
image_name = []
for i in range(no_images):
	image_name.append(sys.argv[i+2])

image = []

# Find the number of columns in the concatenated image

min_no_cols = 5000

for i in range(no_images):
	cur_image = cv2.imread(image_name[i], 1)
	image.append(cur_image)
	no_cols = cur_image.shape[1]
	min_no_cols = min(min_no_cols, no_cols)

# Find the number of rows in the concatenated image

no_rows_total = (no_images - 1)*border_len

for i in range(no_images):
	cur_image = image[i]
	no_rows = cur_image.shape[0]
	no_cols = cur_image.shape[1]
	ratio = float(no_cols)/float(min_no_cols)
	new_no_rows = int(float(no_rows)/ratio)
	no_rows_total += new_no_rows
	appended_image = cv2.resize(cur_image, (min_no_cols, new_no_rows))
	image[i] = appended_image

concatenation = np.zeros((no_rows_total, min_no_cols, 3), np.uint8)
row_start = 0

for i in range(no_images):

	if i != 0:
		row_start += border_len

	cur_image = image[i]
	print cur_image.shape

	no_rows = cur_image.shape[0]
	no_cols = cur_image.shape[1]

	concatenation[row_start:row_start+no_rows,:,:] = cur_image.copy()

	row_start += no_rows

concatenation = cv2.copyMakeBorder(concatenation, border_len, border_len, 
	border_len, border_len, cv2.BORDER_CONSTANT,value = 0)
cv2.imwrite('concatenation.jpg', concatenation)
