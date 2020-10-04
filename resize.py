import numpy as np
import argparse
import imutils
import cv2

# Construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
	help = "Path to the image")
args = vars(ap.parse_args())

# Load the image and show it
image = cv2.imread(args["image"])
cv2.imshow("Original", image)

# We need to keep in mind aspect ratio so the image does
# not look skewed or distorted -- therefore, we calculate
# the ratio of the new image to the old image. Let's make
# our new image have a width of 150 pixels
r = 500.0 / image.shape[1]
dim = (500, int(image.shape[0] * r))

# Perform the actual resizing of the image
resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
cv2.imshow("Resized (Width)", resized)

# What if we wanted to adjust the height of the image? We
# apply the same concept, again keeping in mind the aspect
# ratio, but instead calculating the ratio based on height.
# Let's make the height of the resized image 50 pixels
r = 50.0 / image.shape[0]
dim = (int(image.shape[1] * r), 50)

# Perform the resizing
resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
cv2.imshow("Resized (Height)", resized)


resized = imutils.resize(image, width= 400)
cv2.imshow(" Resized (Width) ",resized)
cv2.waitKey(0)