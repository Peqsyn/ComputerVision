import numpy as np
import cv2

cap = cv2.VideoCapture(1) # video capture source camera (Here webcam of laptop) 

while(1):
    ret,frame = cap.read() # return a single frame in variable `frame`

    # displays frame
    cv2.imshow('frame', frame)

    # 5 ms delay if button is pressed
    i = cv2.waitKey(5) & 0xFF

    # the key refers to ASCII Value 27: escape key
    if i == 27:
        break

    # the key refers to the space bar: takes a picture and saves it
    elif i == 32:
        cv2.imwrite('C:\\Users\\ericl\\Documents\\Gomi\\ComputerVision\\images\\c1.png',frame)

cv2.destroyAllWindows()