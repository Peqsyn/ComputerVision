""" Camera Interfacing.

This module contains all of the necessary components to interaface with
a camera.

Todo:
    * Create image capture function (let it return a numpy array)
    * Get Image
    * Video Feed
    *

"""

import cv2


class CameraAccess:
    """Creates a camera object.

    This object can be used to grab any information required from the
    camera.  Video feeds, single images, etc.

    Attributes:

    
    """

    def detect_cameras(self):
        """Provides a list of potential cameras.
        
        The COM ports will be searched using gphoto2 and cv2 to
        determine what cameras are available.  The potential cameras
        will then be given in a list to the user.

        Args:
            None

        Returns:
            (:obj:'list' of :obj:'str'): each string is the name of a 
                potential camera

        """

        
        return ['default']


    def select_camera(self, camera_name = 'default'):
        """Choose which camera will be used

        detect_cameras will tell the user what cameras are connected.
        One of the listed cameras can then be selected by the user for
        use.  Once selected, the capture, record (if allowed), and other
        camera features will become usable.

        Args:
            camera_name (string): this is a camera name given by
                detect_cameras.

        Returns:
            None

        """

        


    
if __name__ == 'main':

    
