'''

 -- Shifting Mech--

Blue Crew Robotics Team 6153
Authors: Jacob Mealey, Matthew Gallant

'''

import threading
import time
import wpilib
import wpilib.drive

class driveAux (threading.Thread):
    def __init__(self, name, driveController, drivetrain, cube, ramp, joystick, delay):
        threading.Thread.__init__(self)
        self.name = name
        self.drivetrain = drivetrain
        self.driveController = driveController
        self.delay = delay
        self.cubemech = cube
        self.ramp = ramp

    def run(self):
         while True:
            
            time.sleep(self.delay)
            
            if(self.driveController.right_bumper()):
                print("Shift")
                self.drivetrain.shiftGear()
            elif (self.driveController.a() and self.driveController.x()):
                print("Raise Left Ramp")
                self.ramp.raiseLeftRamp()
            elif (self.driveController.a() and self.driveController.b()):
                print("Lower Left Ramp")
                self.ramp.lowerLeftRamp()
            else:
                self.ramp.stopLeft()