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

        # Push buttons for camera switching
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
            Create a new push button with the name of that camera, removing the word Shape[:-5]
            Add that camera to the layout widget
        '''
        for camera in cameras:
            if camera not in self.default_cameras:
                push_button = QPushButton(camera[:-5])
                push_button.setObjectName(camera[:-5])
                self.button_layout.addWidget(push_button)

    '''
        Retrieves the object that triggered the signal
        Sets the camera name to be the objects name and removes the last three characters (_bt)
        Tells maya to look through the given camera name
    '''
    def camera_switch(self):
        button_clicked = self.sender()
        camera_name = button_clicked.objectName()[:-3]
        cmds.lookThru(camera_name)


if __name__ == '__main__':
    app = QApplication.instance()
    if not app:
        app = QApplication(sys.argv)
    
    window = CameraSwitcher()
    window.show()