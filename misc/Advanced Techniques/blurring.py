import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

# blurring meant to reduce noise and detail in an image, tend to lose edges
# within an image

# averaged blur
blurred = np.hstack([cv2.blur(image, (3, 3)),
					 cv2.blur(image, (5, 5)),
					 cv2.blur(image, (7, 7))])
cv2.imshow("Averaged", blurred)
cv2.waitKey(0)

# gaussian blur (more natural)
blurred = np.hstack([cv2.GaussianBlur(image, (3, 3), 0),
					 cv2.GaussianBlur(image, (5, 5), 0),
					 cv2.GaussianBlur(image, (7, 7), 0)])
cv2.imshow("Gaussian", blurred)
cv2.waitKey(0)

# median blur (most effective for removing salt and pepper blur)
blurred = np.hstack([cv2.medianBlur(image, 3),
					 cv2.medianBlur(image, 5),
					 cv2.medianBlur(image, 7)])
cv2.imshow("Median", blurred)
cv2.waitKey(0)

# bilateral blur (reduces noise and maintains edges)
blurred = np.hstack([cv2.bilateralFilter(image, 5, 21, 21),
					 cv2.bilateralFilter(image, 7, 31, 31),
					 cv2.bilateralFilter(image, 9, 41, 41)])
cv2.imshow("Bilateral", blurred)
cv2.waitKey(0)