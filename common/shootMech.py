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

            if (self.subsystemController.right_bumper()):
                self.cubemech.intakeCube()
                print("Intake")
            elif (self.subsystemController.left_bumper()):
                self.cubemech.shootCube()
                print("Shoot")
            else:
                self.cubemech.stop()
