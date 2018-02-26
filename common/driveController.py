'''

 -- Driver Controller System --

Blue Crew Robotics Team 6153
Authors: Jacob Mealey, Matthew Gallant

'''

import threading
import time
import wpilib
import wpilib.drive

class driveController (threading.Thread):
    
    def __init__(self, name, driveController, drivetrain, cube, ramp, joystick, delay):
        threading.Thread.__init__(self)
        self.name = name
        self.driveController = driveController
        self.delay = delay
        self.drivetrain = drivetrain
        self.joystick = joystick
        self.cubemech = cube
        self.ramp = ramp
        self.driveSpeed = 0

    def run(self):

        while True:

            time.sleep(self.delay)

            if (self.driveController.right_bumper()):
                self.drivetrain.shiftGear()
            elif (self.driveController.left_trigger()):
                self.driveSpeed = self.joystick.getRawAxis(2) * -1
            elif (self.driveController.right_trigger()):
                self.driveSpeed = self.joystick.getRawAxis(3)
            elif (self.driveController.a() and self.driveController.x()):
                self.ramp.raiseLeftRamp()
            elif (self.driveController.a() and self.driveController.b()):
                self.ramp.lowerLeftRamp()
            else:
                self.driveSpeed = 0
                self.ramp.stopLeft()
            
            self.drivetrain.arcadeDrive(self.driveSpeed)
