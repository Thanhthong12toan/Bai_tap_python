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
cv2.imshow("Original", image)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("gray",gray)

hsv = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
cv2.imshow("hsv",hsv)

lab = cv2.cvtColor(image,cv2.COLOR_BGR2LAB)
cv2.imshow("lab",lab)

cv2.waitKey(0)
