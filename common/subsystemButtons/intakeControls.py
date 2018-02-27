import threading
import time
import wpilib
import wpilib.drive

class intakeControls(threading.Thread):

    def __init__(self, cube, controller, joystick, delay):
        threading.Thread.__init__(self)
        self.cubemech = cube
        self.subsystemController = controller
        self.delay = delay

    def run(self):
        while True:

            time.sleep(self.delay)

            if (self.subsystemController.right_bumper()):
                self.cubemech.intakeCube()
            elif (self.subsystemController.left_bumper()):
                self.cubemech.shootCube()
            else:
                self.cubemech.stop()
            