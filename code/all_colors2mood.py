import cv2
import numpy as np
import sys
import math
import os

def make_np(blue, green, red):
	return np.array([blue, green, red])

def colorDst(color1, color2):
	diff = np.subtract(color1, color2)
	squares = np.square(diff)
	sum_of_squares = np.sum(squares)
	return math.sqrt(sum_of_squares)

def assignColor(pixel):
	best_color = np.zeros((3), np.uint8)
	min_dist = math.sqrt(3*256*256)
	id_best = 0

	colors = []
	colors.append(make_np(0,0,0)) # black
	colors.append(make_np(255,0,0)) # blue
	colors.append(make_np(0,255,0)) # green
	colors.append(make_np(0,0,255)) # red
	colors.append(make_np(255,255,0)) # cyan
	colors.append(make_np(255,0,255)) # magenta
	colors.append(make_np(0,255,255)) # yellow
	colors.append(make_np(255,255,255)) # white

	for idx in range(8):
		color = colors[idx]
		dist = colorDst(color, pixel)
		if dist < min_dist:
			best_color = color.copy()
			min_dist = dist
			id_best = idx

	best_blue = best_color[0] + pixel[0]
	best_blue /= 2

	best_green = best_color[1] + pixel[1]
	best_green /= 2

	best_red = best_color[2] + pixel[2]
	best_red /= 2

	return make_np(best_blue, best_green, best_red), id_best

def getBestColorMatch(image):
	color_image = image.copy()
	no_rows = color_image.shape[0]
	no_cols = color_image.shape[1]
	bins = np.array([0, 0, 0, 0, 0, 0, 0, 0])
	for row in range(no_rows):
		for col in range(no_cols):
			pixel = color_image[row, col]
			color_pixel, id_col = assignColor(pixel)
			color_image[row, col] = color_pixel.copy()

	return color_image

def colorAllImagesIn(path):

	files = filter((lambda x: x.endswith('.jpg')), os.listdir(path))

	max_allow = 300.0
	for image_name in files:
		print 'Processing', image_name
		image = cv2.imread(path + image_name)
		no_rows = image.shape[0]
		no_cols = image.shape[1]

		if no_rows > max_allow:
			ratio = float(no_rows)/max_allow
			n_rows = int(float(no_rows)/ratio)
			n_cols = int(float(no_cols)/ratio)
			image = cv2.resize(image, (n_cols, n_rows))

		color_image = getBestColorMatch(image)
		cv2.imwrite('mood_' + image_name, color_image)
		print 'Done with', image_name

path = sys.argv[1]
colorAllImagesIn(path)















