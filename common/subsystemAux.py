'''

 -- Subsystem Aux --

Blue Crew Robotics Team 6153
Authors: Jacob Mealey, Matthew Gallant

'''

import threading
import time
import wpilib
import wpilib.drive

class subsystemAux (threading.Thread):
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

            if (self.subsystemController.a() and self.subsystemController.y()):
                print("deploy ramps")
                self.ramp.deployRamps()
            elif (self.subsystemController.a() and self.subsystemController.x()):
                print("raise right ramp")
                self.ramp.raiseRightRamp()
            elif (self.subsystemController.a() and self.subsystemController.b()):
                print("lower right ramp")
                self.ramp.lowerRightRamp()
            elif (self.subsystemController.b()):
                print("clamp baby")
                self.cubemech.clampCube()
            else:
                self.ramp.stopRight()