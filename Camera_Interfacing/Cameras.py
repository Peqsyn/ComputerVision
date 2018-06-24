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

    def __init__(self):
        """Initialize all object variables

        Args:
            None

        Returns:
            None

        """

        # cameras is a dictionary which will contain the name of the
        #   each camera as well as the access method and, in the case of
        #   opencv, will provide the camera number.
        #
        # Opencv will have the following dictionary layout:
        #       'cv2': ['camera_name_1': port, 'camera_name_2': port, ...] 
        self.cameras = []

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

        # Initialize opencv cameras
        try:
            camera_num = 0
            while(True):
                
        self.cameras
        
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

    def _find_opencv_cameras(self):
        """Find all of the default cameras

        Th
        


    
if __name__ == 'main':

    camera_1 = CameraAccess()
    camera_1.detect_cameras()
    camera_1.select_camera()
