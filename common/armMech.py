'''

 -- Arm Mech --

Blue Crew Robotics Team 6153
Authors: Jacob Mealey, Matthew Gallant

'''

import threading
import time
import wpilib
import wpilib.drive

class armMech (threading.Thread):

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

            while (self.subsystemController.right_trigger()):
                self.cubemech.liftArm()
                print("Lift Arm")
                if(self.subsystemController.right_trigger() == False):
                    break
            while (self.subsystemController.left_trigger()):
                self.cubemech.lowerArm()
                print("Lower Arm")
                if(self.subsystemController.left_trigger() == False):
                    break
            if (self.subsystemController.b()):
                print("Clamp Cube")
                self.cubemech.clampCube()
                time.sleep(0.5)
            else:
                self.cubemech.stop()
