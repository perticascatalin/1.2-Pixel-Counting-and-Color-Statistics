import cv2
import sys

image_name = sys.argv[1]
image = cv2.imread(image_name)
pixels_on_top = int(sys.argv[2])
pixels_on_bottom = int(sys.argv[3])
pixels_on_left = int(sys.argv[4])
pixels_on_right = int(sys.argv[5])

new_image = cv2.copyMakeBorder(image, 
	pixels_on_top, pixels_on_bottom, 
	pixels_on_left, pixels_on_right, cv2.BORDER_CONSTANT, value = 0)

cv2.imwrite('with_border.jpg', new_image)