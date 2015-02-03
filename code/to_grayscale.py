import cv2
import sys

image_name = sys.argv[1]
image = cv2.imread(image_name, 0)
cv2.imwrite(image_name, image)