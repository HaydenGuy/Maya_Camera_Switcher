import sys

import maya.cmds as cmds

from PySide6.QtWidgets import QMainWindow, QApplication, QPushButton
import Maya_Camera_Switcher.UI.camera_switcher_ui as ui 

class CameraSwitcher(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = ui.Ui_camera_switcher()
        self.ui.setupUi(self)

        self.default_cameras = ('perspShape', 'topShape', 'frontShape', 'sideShape')
        self.added_cameras = []
        self.list_all_cameras()

        # Triggers the create_camera method if Create... Camera is triggered
        self.ui.action_create_camera.triggered.connect(self.create_camera)

        # Push buttons for default camera switching
        self.ui.persp_bt.clicked.connect(self.camera_switch)
        self.ui.top_bt.clicked.connect(self.camera_switch)
        self.ui.front_bt.clicked.connect(self.camera_switch)
        self.ui.side_bt.clicked.connect(self.camera_switch)

    # Creates a camera and runs the list_all_cameras to update the push buttons
    def create_camera(self):
        cmds.camera()[0]
        self.list_all_cameras()

    # Creates push buttons for all cameras in the scene besides the defaults
    def list_all_cameras(self):
        # Gets a list of all the cameras in the scene
        cameras = cmds.ls(type='camera')

        '''
            Iterate through the list of cameras and if the camera is not a default or added camera
            camera_name is the name of the camera, removing the word Shape
            Create a new push button with the name of the camera_name
            Add that camera to the layout widget
            Append the camera to the list of added cameras
        '''
        for camera in cameras:
            if camera not in self.default_cameras and camera not in self.added_cameras:
                camera_name = camera.replace('Shape', '')
                push_button = QPushButton(camera_name, self)
                push_button.setObjectName(camera_name)
                self.ui.button_layout.addWidget(push_button)
                self.added_cameras.append(camera)

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