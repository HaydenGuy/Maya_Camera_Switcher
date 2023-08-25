import sys
# Imports the folder path. Allows for modular UI
sys.path.append('/mnt/32346261-2a77-4ea4-ad97-df46c23e0f72/Maya_Scripts/Camera_Switcher')

import maya.cmds as cmds

from PySide2.QtWidgets import QMainWindow, QApplication, QPushButton
from UI.Ui_camera_switcher import Ui_camera_switcher

class CameraSwitcher(QMainWindow, Ui_camera_switcher):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.default_cameras = ('perspShape', 'topShape', 'frontShape', 'sideShape')
        self.list_all_cameras()

        # Push buttons for default camera switching
        self.persp_bt.clicked.connect(self.camera_switch)
        self.top_bt.clicked.connect(self.camera_switch)
        self.front_bt.clicked.connect(self.camera_switch)
        self.side_bt.clicked.connect(self.camera_switch)

    # Creates push buttons for all cameras in the scene besides the defaults
    def list_all_cameras(self):
        # Gets a list of all the cameras in the scene
        cameras = cmds.ls(type='camera')

        '''
            Iterate through the list of cameras and if the camera is not one of the defaults
            camera_name is the name of the camera, removing the word Shape
            Create a new push button with the name of the camera_name
            Add that camera to the layout widget
        '''
        for camera in cameras:
            if camera not in self.default_cameras:
                camera_name = camera.replace('Shape', '')
                push_button = QPushButton(camera_name, self)
                push_button.setObjectName(camera_name)
                self.button_layout.addWidget(push_button)  

                # Connecting the new push button to the camera_switch method
                push_button.clicked.connect(self.camera_switch)
                
    '''
        Retrieves the object that triggered the signal
        Sets the camera name to be the objects name and replaces _bt if its present (default buttons)
        Tells maya to look through the given camera name
    '''
    def camera_switch(self):
        camera = self.sender()
        camera_name = camera.objectName().replace('_bt', '')
        cmds.lookThru(camera_name)


if __name__ == '__main__':
    app = QApplication.instance()
    if not app:
        app = QApplication(sys.argv)
    
    window = CameraSwitcher()
    window.show()