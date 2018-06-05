import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# improves the contrast of an image by stretching the distribution of pixels
eq = cv2.equalizeHist(image)

cv2.imshow('Histogram Equalization', np.hstack([image, eq]))
cv2.waitKey(0)