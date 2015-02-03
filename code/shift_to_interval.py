import cv2
import sys
import numpy as np

image_name = sys.argv[1]
image = cv2.imread(image_name, 0)

low = int(sys.argv[2])
high = int(sys.argv[3])

low_img = min(image.ravel())
high_img = max(image.ravel())

print low_img, high_img

diff = float(high - low)
diff_img = float(high_img - low_img)

no_rows = image.shape[0]
no_cols = image.shape[1]

for row in range(no_rows):
	for col in range(no_cols):
		temp = (float(image[row, col]) - float(low_img))/diff_img
		image[row, col] = int(temp * diff + float(low))

low_img = min(image.ravel())
high_img = max(image.ravel())

print low_img, high_img

#cv2.imshow('shifted', image)
#cv2.waitKey()

cv2.imwrite('shift_' + str(low) + '_' + str(high) + '.jpg', image)