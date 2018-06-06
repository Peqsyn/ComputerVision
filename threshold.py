import numpy as np
import cv2
from matplotlib import pyplot as plt

cap = cv2.VideoCapture(1)

while(1):
    # take each frame
    _, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

    # displays frame
    cv2.imshow('frame', frame)
    cv2.imshow('thresh', thresh)

    i = cv2.waitKey(5) & 0xFF

    # the key refers to ASCII Value 27: esc key
    if i == 27:
        break

cv2.destroyAllWindows()