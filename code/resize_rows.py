# Resizes an image with a given ratio

import cv2
import numpy as np
import sys

image_name = sys.argv[1]
desired_rows = int(sys.argv[2])

image = cv2.imread(image_name, 1)
rows, cols, ch = image.shape
ratio = float(rows)/float(desired_rows)
n_rows = int(float(rows)/ratio)
n_cols = int(float(cols)/ratio)
image = cv2.resize(image, (n_cols, n_rows))
cv2.imwrite('resized.jpg', image)