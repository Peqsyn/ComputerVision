import argparse # arg parse to handle parsing command line arguments
import cv2

# handles command line arguments
ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True, help='Path to the image')
args = vars(ap.parse_args())

# returns numpy array representing image
image = cv2.imread(args['image']) 

# dimensions of the image
print('width: {} pixels'.format(image.shape[1]))
print('height: {} pixels'.format(image.shape[0]))
print('channels: {}'.format(image.shape[2]))

# displays image on screen
cv2.imshow('Image', image)

# waits for keypress until unpausing execution
cv2.waitKey(0)

# saves the image in a jpg format
cv2.imwrite('newimage.jpg', image)