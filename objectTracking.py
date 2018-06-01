#! python3
import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(1):
    # take each frame
    _, frame = cap.read()

    # convert from RGB to HSV, HSV is better for image processing
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # color to define https://www.rapidtables.com/convert/color/rgb-to-hsv.html
    # black
    x1, y1, z1 = 0, 0, 0
    x2, y2, z2 = 180, 255, 30


    # define range of color in HSV
    lower_color = np.array([x1, y1, z1])
    upper_color = np.array([x2, y2, z2])

    # threshold hsv image to get only the defined color
    mask = cv2.inRange(hsv, lower_color, upper_color)

    # bitwise-and mask and original image
    res = cv2.bitwise_and(frame, frame, mask= mask)

    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)
    i = cv2.waitKey(5) & 0xFF

    # the key refers to ASCII Value 32: space key
    if i == 32:
        break

cv2.destroyAllWindows()