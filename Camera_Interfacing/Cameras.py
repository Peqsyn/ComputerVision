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
        #     'cv2': ['camera_name_1': port, 'camera_name_2': port, ...]
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
        # Create dictionary of all connected cameras
        self.cameras = {}

        # Add openCV cameras
        self.cameras.update(self._find_opencv_cameras())

        return self.cameras


    def _find_opencv_cameras(self):
        """Find all of the default cameras

        Use opencv to test all of the camera ports from zero on to see
        how many cameras are available for use.  A list of possible 
        cameras is then compiled into a dictionary as prescribed below

        Opencv will have the following dictionary layout:
               ('cv2', ['camera_1': port, 'camera_2': port, ...]) 
        
        Args:
            None
        
        Returns:
            camera_list (dictionary entry): this can be used to produce 
                a dictionary of potential cameras.

        """

        camera_info = {'cv2': {}}

        camera_num = 0
        while(True):
            # Test the camera
            cap = cv2.VideoCapture(camera_num)
            if(not cap.isOpened()):
                cap.release()
                break
            cap.open(camera_num)
            cap.release()

            # Document camera info
            camera_info['cv2'].update({'camera_%s' % str(camera_num): camera_num})

            # Test next camera
            camera_num += 1
            
        return camera_info

        
    def select_camera(self, detection_method='cv2', 
                            camera_name='camera_0'):
        """Choose which camera will be used

        detect_cameras will tell the user what cameras are connected.
        One of the listed cameras can then be selected by the user for
        use.  Once selected, the capture, record (if allowed), and other
        camera features will become usable.

        Args:
            detection_method (string): Describes the detection method
                used for detecting the cameras.  Possible methods are
                ['cv2',...more to be added later]
            camera_name (string): This is a camera name given by
                detect_cameras.

        Returns:
            None

        """

        self.camera_connection = cv2.VideoCapture(
            self.cameras[detection_method][camera_name])
                

    def capture_image(self, file_name, file_path):
        """Take a picture and save it

        When called, this function takes the current frame and saves it
        with the given file name in the specified folder.  

        Args:
            file_name (string): The name of the file
            file_path (string): The path of the folder where the image
                will be saved.  ***Do not place a backslash after the
                folder name***

        Returns:
            None

        """
        # Read the frame
        ret, frame = self.camera_connection.read()
        
        # Write the image
        cv2.imwrite('%s/%s' % (file_path, file_name), frame)


    
if __name__ == '__main__':

    print('Starting Now')
    
    camera_1 = CameraAccess()
    print(camera_1.detect_cameras())
    camera_1.select_camera('cv2', 'camera_0')
    camera_1.capture_image('test.jpg', 'C:/Users/Peter/Pictures')

    print('Program done')
