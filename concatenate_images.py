# Run: python <border_length> <image_name_1> <image_name_2> ...
# Concatenates images horizontally
# All images are resized to have the number of rows equal the minimum among all images

import cv2
import sys
import numpy as np

border_len = int(sys.argv[1])
no_images = len(sys.argv) - 2
image_name = []
for i in range(no_images):
	image_name.append(sys.argv[i+2])

image = []

# Find the number of rows in the concatenated image

min_no_rows = 5000

for i in range(no_images):
	cur_image = cv2.imread(image_name[i], 1)
	image.append(cur_image)
	no_rows = cur_image.shape[0]
	min_no_rows = min(min_no_rows, no_rows)

# Find the number of columns in the concatenated image

no_cols_total = (no_images - 1)*border_len

for i in range(no_images):
	cur_image = image[i]
	no_rows = cur_image.shape[0]
	no_cols = cur_image.shape[1]
	ratio = float(no_rows)/float(min_no_rows)
	new_no_cols = int(float(no_cols)/ratio)
	no_cols_total += new_no_cols
	appended_image = cv2.resize(cur_image, (new_no_cols, min_no_rows))
	image[i] = appended_image

concatenation = np.zeros((min_no_rows, no_cols_total, 3), np.uint8)
col_start = 0

for i in range(no_images):

	if i != 0:
		col_start += border_len

	cur_image = image[i]

	no_rows = cur_image.shape[0]
	no_cols = cur_image.shape[1]

	concatenation[:,col_start:col_start+no_cols,:] = cur_image.copy()

	col_start += no_cols

concatenation = cv2.copyMakeBorder(concatenation, border_len, border_len, 
	border_len, border_len, cv2.BORDER_CONSTANT,value = 0)
cv2.imwrite('concatenation.jpg', concatenation)
