# Run: python histogram_output.py <image_name>
# Outputs image histogram for grayscale and BGR components separately
# Obtained images saved under: 'gray_hist.jpg', 'blue_hist.jpg', 'green_hist.jpg', 'red_hist.jpg'

import cv2
import sys
import numpy as np
from matplotlib import pyplot as plt

def hist_output_grayscale(image):
	plt.hist(image.ravel(),256,[0,256], color = 'gray')
	plt.savefig('gray_hist.jpg')
	plt.clf()

def hist_output_BGR(image):
	blue_component = image[:,:,0:1]
	green_component = image[:,:,1:2]
	red_component = image[:,:,2:3]
	plt.hist(blue_component.ravel(),256,[0,256], color = 'blue')
	plt.savefig('blue_hist.jpg')
	plt.clf()
	plt.hist(green_component.ravel(),256,[0,256], color = 'green')
	plt.savefig('green_hist.jpg')
	plt.clf()
	plt.hist(red_component.ravel(),256,[0,256], color = 'red')
	plt.savefig('red_hist.jpg')
	plt.clf()

image_name = sys.argv[1]

grayscale = cv2.imread(image_name, 0)
BGR = cv2.imread(image_name, 1)
hist_output_grayscale(grayscale)
hist_output_BGR(BGR)

#hist = cv2.calcHist([img], [0], None, [256], [0,256])
#plt.plot(hist)
#plt.show()