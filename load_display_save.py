from __future__ import print_function
import argparse
import numpy as np
from argparse import ArgumentParser

import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="path to input image")
args = vars(ap.parse_args())
image = cv2.imread(args["image"])
print("width: {} pixels".format(image.shape[1]))
print("height: {} pixels".format(image.shape[0]))
print("channels: {}".format(image.shape[2]))

cv2.imshow("Image",image)

cv2.imwrite("newimage.jpg",image)

(b, g, r) = image[0, 0]
print("Pixel at (0, 0) - Red: {}, Green: {}, Blue: {}".format(r,
g, b))
image[0, 0] = (0, 0, 255)
(b, g, r) = image[0, 0]
print("Pixel at (0, 0) - Red: {}, Green: {}, Blue: {}".format(r,
g, b))


corner = image[0:100,0:100]
cv2.imshow("corner",corner)

image[0:100,0:100]=(15,0,18)

cv2.imshow("updated",image)

# Initialize our canvas as a 300x300 with 3 channels,
# Red, Green, and Blue, with a black background
canvas = np.zeros((300, 300, 3), dtype = "uint8")

# Draw a green line from the top-left corner of our canvas
# to the bottom-right
green = (0, 255, 0)
cv2.line(canvas, (0, 0), (300, 300), green)
cv2.imshow("Canvas", canvas)

# Now, draw a 3 pixel thick red line from the top-right
# corner to the bottom-left
red = (0,0,255)
cv2.line(canvas,(300,0),(0,300),red,3)

cv2.rectangle(canvas, (10, 10), (60, 60), green)
cv2.imshow("Canvas",canvas)

# Draw another rectangle, this time we'll make it red and
# 5 pixels thick
cv2.rectangle(canvas, (50, 200), (200, 225), red, 5)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# Let's draw one last rectangle: blue and filled in
blue = (255, 0, 0)
cv2.rectangle(canvas, (200, 50), (225, 125), blue, -1)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# Reset our canvas and draw a white circle at the center
# of the canvas with increasing radii - from 25 pixels to
# 150 pixels
canvas = np.zeros((300, 300, 3), dtype = "uint8")
(centerX, centerY) = (canvas.shape[1] // 2, canvas.shape[0] // 2)
white = (255, 255, 255)

for r in range(0, 150,25):
	cv2.circle(canvas, (centerX, centerY), r, white)

cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# Let's go crazy and draw 25 random circles
for i in range(0, 25):
	# randomly generate a radius size between 5 and 200,
	# generate a random color, and then pick a random
	# point on our canvas where the circle will be drawn
	radius = np.random.randint(5, high = 200)
	color = np.random.randint(0, high = 256, size = (3,)).tolist()
	pt = np.random.randint(0, high = 300, size = (2,))

	# draw our random circle
	cv2.circle(canvas, tuple(pt), radius, color, -1)

# Show our masterpiece
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
