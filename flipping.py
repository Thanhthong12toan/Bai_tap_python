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

flipped = cv2.flip(image,1)
cv2.imshow("Flipped Horizontally",flipped)

flipped = cv2.flip(image,0)
cv2.imshow("Flipped Vertically",flipped)

flipped = cv2.flip(image,-1)
cv2.imshow("Flipped Horizontally & Vertically",flipped)


#crop image
cropped = image[30:120 , 240:335]
cv2.imshow("T-Rex Face", cropped)

cv2.waitKey(0)