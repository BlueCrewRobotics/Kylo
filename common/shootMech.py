'''

 -- Shoot Mech --

Blue Crew Robotics Team 6153
Authors: Jacob Mealey, Matthew Gallant

'''

import threading
import time
import wpilib
import wpilib.drive

class shootMech (threading.Thread):

    def __init__(self, name, controller, joystick, cube, ramp, delay):
        threading.Thread.__init__(self)
        self.name = name
        self.subsystemController = controller
        self.delay = delay
        self.cubemech = cube
        self.ramp = ramp

    def run(self):
        while True:
            
            time.sleep(self.delay)

            while (self.subsystemController.right_bumper()):
                self.cubemech.intakeCube()
                print("Intake")
                if (self.subsystemController.right_bumper() == False):
                    break
            while (self.subsystemController.left_bumper()):
                self.cubemech.shootCube()
                print("Shoot")
                if (self.subsystemController.left_bumper() == False):
                    break

