## Pixel Counting and Color Statistics - Part I

### Gathering Information from Color

In this article, I would like to explore deeper what one can do with OpenCV only by analyzing how often certain colors appear and in what proportions they are to be found in different types of images.

*How reliable do you think color is?*

*What can it tell us about an image?*

*What not?*

Color is very sensitive to lighting conditions(illumination). While a colorful object may seem black at night, a piece of dark metal could appear white and shiny on a sunny day. We are able to acknowledge this matter of fact, but for a machine this would be way more difficult to grasp.

Consequently, grayscale images are used more often when applying object recognition algorithms. However, using color as a simple feature that can be extracted from images is a very good way to prepare yourself before learning about more complex features.

Take a look at this image which consists of sand only. 

![alt](http://www.weheartcv.com/wp-content/uploads/2014/12/illumination.jpg)

The sand is perceived under different illumination conditions:  

**Normal sand** - control condition, yellow-light brown color  

**Sand under the water** - reflects more light and thus appears shinier, a slight tendency towards blue  

**Sand under the shadow** - receives less light from the sun and so appears darker, a strong tendency towards black


| Condition             | Average intensity |
| --------------------- | :---------------: |
| Sand under the water  | 76%               |
| Normal sand           | 66%               |
| Sand under the shadow | 30%               |

So sand can be visually perceived in variations of yellow, blue, black and possibly other colors. This proves just how unreliable color is for automated(made by computers) detection.

Before reading further, take a moment to think about the following questions.

*How do you distinguish between the foreground and background of an image?*  


foreground = hand  
![alt](http://www.weheartcv.com/wp-content/uploads/2014/12/resized_hand.jpg)

foreground = coins  
![alt](http://www.weheartcv.com/wp-content/uploads/2014/12/resized_coins.jpg)

*How do you know whether a photo is taken during the day or during the night?*  



![alt](http://www.weheartcv.com/wp-content/uploads/2014/12/resized_day.jpg)

![alt](http://www.weheartcv.com/wp-content/uploads/2014/12/resized_night.jpg)
  
*Or even whether Picasso's paintings are from his Blue or Rose Period?*

![alt](http://www.weheartcv.com/wp-content/uploads/2014/12/blue1-e1419002740774.jpg)  
[Source: wikipedia](http://upload.wikimedia.org/wikipedia/en/b/bc/Old_guitarist_chicago.jpg)

![alt](http://www.weheartcv.com/wp-content/uploads/2014/12/rose-e1419002757923.jpg)  
[Source: wikipedia](http://upload.wikimedia.org/wikipedia/en/a/a3/Picasso_The_Actor_1904.JPG)

### Histograms 

![alt](http://www.weheartcv.com/wp-content/uploads/2014/12/coins_p_hist.jpg)

Histograms are a good way to visualize the different amounts of color/intensity in images. Do you know how to create a histogram? It is fairly similar to ordering some objects by their categories and then losing all information specific to the object, while only preserving information about the category. The pixels in an image have a color and a position. If the categories were colors, then the image histogram would lose the information about where pixels are located and would only be able to tell how many pixels of a certain color there are.

Long story short, a histogram counts the number of pixels of a certain type and displays their numbers in a graph.

![alt](http://www.weheartcv.com/wp-content/uploads/2014/12/hand_p_hist.jpg)

*Did you notice, while looking at the two histograms, the two peaks and the valley between them?*

*What do you think they might represent?*

In the image with the coins, the first peak stands for the pixels representing coins, the **foreground**, while the second one represents the **background** pixels. Notice that the gap between them is more visible than in the image with the hand.

*Why do you think there are more pixels in the gap between the peaks in the second image?*

The pixels that are associated with the **gap** have **transitional intensities** between the brightest and darkest objects in the image. We can notice them in the left part of the image, where the hand is slightly shadowed. Still, foreground and background can be separated quite easily.

These **2-peaks** type of histograms are called **bimodal**. This name comes from statistics and it refers to probability distributions. The mode is the maxima of the distribution. A distribution with two maximas will have 2 modes -> bimodal, while one with 3 maximas will be called trimodal and so on.  

![alt](http://www.weheartcv.com/wp-content/uploads/2014/12/unimodal_expl.jpg)

![alt](http://www.weheartcv.com/wp-content/uploads/2014/12/bimodal_expl.jpg)

![alt](http://www.weheartcv.com/wp-content/uploads/2014/12/trimodal_expl.jpg)

**Histograms in OpenCV**:

Short version, for **one image and one channel**:
```python
cv2.calcHist([image], [channel], mask, 
	[no_bins], [start_bin_inclusive, end_bin_exclusive])
```  


**Use for grayscale vs. BGR**

In case you are working with a grayscale image, simply replace ```channel``` by 0. With BGR images, you can specify 0, 1 or 2 for blue, green and red channels.

Longer version, for **more images and more channels**:
```python
cv2.calcHist([image1, image2, ...], 
	[channel1, channel2, ...], 
	mask, [no_bins_channel1, no_bins_channel2, ...], 
	[low_channel1, high_channel1, low_channel2, high_channel2, ...])
```

[spoiler title='Return format' collapse_link='true']
This will return an ```no_bins_channel1 x no_bins_channel2 x ... ``` array. The number of dimensions is equal to the length of the arrays in the 2nd and 4th arguments.
[/spoiler]

[spoiler title='Images format' collapse_link='true']
Note that the images specified must have the same size and depth.
[/spoiler]

[spoiler title='Channels format' collapse_link='true']
For grayscale images, 0 will refer to the only channel in the first image, 1 will refer to the only channel in the second one and so on. For BGR images, 0, 1 and 2 will be used for blue, green and red channels in the first image, 3, 4 and 5 for the second image and so on.
[/spoiler]

[spoiler title='Mask format' collapse_link='true']
This is an optional field, but if specified, it must have the same size as the images. All 0-valued pixels will be discarded when computing the histogram.
[/spoiler]

[spoiler title='Bins format' collapse_link='true']
An array specifying into how many bins/categories the pixels in the corresponding channel are divided.
[/spoiler]

[spoiler title='Ranges format' collapse_link='true']
This refers to this part ```[low_channel1, high_channel1, low_channel2, high_channel2, ...]```. For color counting, the low's will be 0 and the high's 256. But if you work with something else, this changes. For example, if you simply wish to count only the brighter half of the color spectrum, you would specify low to be 128 and high to be 256. Note that this will also affect the number of bins.
[/spoiler]

For a more detailed explanation, take a look at the [documentation](http://docs.opencv.org/modules/imgproc/doc/histograms.html).  


**Visualizing a histogram**

The simplest way to create an image from the obtained histogram is to use the plot function from the Matplotlib library.

Grayscale image histogram:
```python
from matplotlib import pyplot as plt

image_name = sys.argv[1]
image = cv2.imread(image_name, 0)

hist = cv2.calcHist([image], [0], None, [256], [0,256])

# Plotting the histogram and saving the figure
plt.plot(hist)
plt.savefig('hist_' + image_name)
```

Matplotlib even has a method that can plot directly the histogram:

```python
plt.hist(image.ravel(),256,[0,256], color = 'gray')
plt.savefig('hist_' + image_name)
```

Alternatively, this can also be done using an OpenCV method:
```python
cv2.polylines(image, points, is_closed, color)
```
but you will need to convert the histogram into an array of points. The code [here](https://code.google.com/p/pythonxy/source/browse/src/python/OpenCV/DOC/samples/python2/hist.py?repo=xy-27&r=cd6bf12fae7ae496d581794b32fd9ac75b4eb366) should do exactly this.

The Numpy library also provides methods for getting histograms. You can read more about ```numpy.histogram()``` and ```numpy.bincount()``` [here](http://docs.opencv.org/trunk/doc/py_tutorials/py_imgproc/py_histograms/py_histogram_begins/py_histogram_begins.html) and [here](http://docs.scipy.org/doc/numpy/reference/generated/numpy.histogram.html).

### Counting pixels

Having investigated what histograms are and how to obtain them in Python, let us see whether we can decide between images depicting Blue and Rose Periods and between photos taken during day and at night, just by looking at their histograms.

For our first example, we need to define what blue-ish and red-ish pixels are and count them. *How would you define them?*

To keep this simple, count any pixel with ```blue_component >= 100``` as blue-ish and those with ```red_component >= 100``` as red-ish. This is a little bit incorrect, but proves the point for our case. In the following sections we will come up with a better definition.

![alt](http://www.weheartcv.com/wp-content/uploads/2014/12/rose_p_hist.jpg)

Count (blue-ish) ->  77027 pixels  
Count (red-ish)  -> 178872 pixels

Percentage(blue-ish) -> 19%  
Percentage(red-ish)  -> 45%  

![alt](http://www.weheartcv.com/wp-content/uploads/2014/12/blue_p_hist.jpg)

Count (blue-ish) -> 184052 pixels  
Count (red-ish)  ->  54010 pixels

Percentage (blue-ish) -> 46%  
Percentage (red-ish)  -> 13% 

You can see that even with our clumsy definition of blue and red, it is already obvious from the 4 numbers which image belongs to which period.

Before plotting the histograms of the two images, it is advised to scale them such that they have approximately the same number of pixels or to divide the numbers by the total number of pixels(compute percentages instead). Otherwise, a small patch of blue pixels in the image that is supposed to contain less blue might make you think it is the other way around if the image with the blue patch is much larger than the second one. 

[spoiler title='How to scale images to same number of pixels' collapse_link='true']

**Simple maths**:

1:``new_no_rows * new_no_cols = min_no_pix``

2:``new_no_rows = no_rows/ratio``  
3:``new_no_cols = no_cols/ratio``

By replacing 2 and 3 in 1, we get

4:``(no_rows * no_cols)/ratio^2 = min_no_pix``

Which leads to

5: ``ratio = sqrt((no_rows * no_cols)/min_no_pix)``

**Source code**:

```python
# Run: python scale_same_no_pix.py <image_name1> <image_name2> ...

import cv2
import sys
import math

# Get the number of images provided

no_images = len(sys.argv) - 1
image_name = []

# Get all the names of the images that we want to resize to a common number of pixels

for i in range(no_images):
	cur_name = sys.argv[i+1]
	image_name.append(cur_name)

image = []

for i in range(no_images):
	cur_image = cv2.imread(image_name[i])
	image.append(cur_image)

# Initialize minimum number of pixels to the one from the first image

min_no_pix = image[0].shape[0] * image[0].shape[1]

# Find out the minimum number of pixels out of all images

for i in range(no_images):
	no_rows = image[i].shape[0]
	no_cols = image[i].shape[1]
	min_no_pix = min(min_no_pix, no_rows * no_cols) 

# Resize all images so that they contain about the same number of pixels as the minimum number of pixels

for i in range(no_images):
	no_rows = image[i].shape[0]
	no_cols = image[i].shape[1]
	ratio = math.sqrt((float(no_rows)*float(no_cols))/float(min_no_pix))
	n_rows = int(float(no_rows)/ratio)
	n_cols = int(float(no_cols)/ratio)
	image[i] = cv2.resize(image[i], (n_cols, n_rows))
	cv2.imwrite(str(i) + '.jpg', image[i])
```

[/spoiler]

For our second example, we do not need to take color so much into account as intensity. So let us work with the grayscale version of the image when plotting the histogram. We can use a similar definition for bright pixels as previously ```grayscale_component >= 100```.

![alt](http://www.weheartcv.com/wp-content/uploads/2014/12/day_p_hist.jpg)

Percentage (bright) -> 53%  

![alt](http://www.weheartcv.com/wp-content/uploads/2014/12/night_p_hist.jpg)

Percentage (bright) -> 12%

If you want to look at images and histograms at the same time, you might find this useful:

[spoiler title='How to concatenate more images together' collapse_link='true']

```python
# Run: python concatenate_images.py <border_length> <image_name_1> <image_name_2> ...
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
```
[/spoiler]
