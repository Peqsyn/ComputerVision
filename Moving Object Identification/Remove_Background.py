# Remove_Background.py
# --------------------
# Purpose: This file contains all of the functions required
#           to remove a constant background from an image.
#
# Important Information: ***
#

import numpy, cv2, os


# Image_Layers
# ------------
# Purpose: This object splits images into layers given a background image and another image.
#           The front layer contains all of the new items from the previous layers. Thus, 
#           every time a new image is added it will generate a new layer of items.
#
class Image_Layers:

    # There needs to be at least one layer to start
    def __init__(self, background_path = None, foreground_path = None):

        if(background_path == None and foreground_path == None):
            # Default to the first tiff in the pictures directory
            image_path = os.path.expanduser('~/Pictures/')
            for picture in os.listdir(image_path):
                if(picture.endswith('.TIF')):
                    background_path = picture
                    break

        if(foreground_path == None):
            foreground_path == background_path

        if(background_path == None):
            background_path == foreground_path

        # Create image object for background (16-bit color depth)
        background = cv2.imread(background_path, cv2.IMREAD_ANYDEPTH)
        # Create image object for foreground (16-bit color depth)
        foreground = cv2.imread(foreground_path, cv2.IMREAD_ANYDEPTH)

        #*** Seperate the two layers ***#

        self.layers = [background, foreground] 

    def add_layer(self, foreground_path):
        foreground = cv2.imread(foreground_path, cv2.IMREAD_ANYDEPTH)

        



    
image_path = os.getcwd()
folder = '/TIFF_Images/'
image_name = 'DSC_0041'
image_format = '.TIF'
background_path = image_path + folder + image_name + image_format

layers = Image_Layers(background_path)

cv2.imshow('image', layers.layers[0])
cv2.waitKey(0)
cv2.destroyAllWindows()

