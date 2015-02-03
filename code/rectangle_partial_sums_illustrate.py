import cv2
import numpy as np
import sys

no_rows = int(sys.argv[1])
no_cols = int(sys.argv[2])
no_pix = int(sys.argv[3])
border_len = int(sys.argv[4])

n_rows = no_rows * no_pix + (no_rows - 1) * border_len
n_cols = no_cols * no_pix + (no_cols - 1) * border_len

image = 255 * np.ones((n_rows, n_cols, 3), np.uint8)

# place borders first

for row in range(n_rows):
	for col in range(n_cols):
		

