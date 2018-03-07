'''

 -- Driver Controller System --

Blue Crew Robotics Team 6153
Authors: Jacob Mealey, Matthew Gallant

'''

import threading
import time
import wpilib
import wpilib.drive

class driveControls (threading.Thread):
    
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
        self.turnSpeed = 0

    def run(self):

        while True:

            time.sleep(self.delay)
            
            if (self.driveController.y() and self.joystick.getX() > 0):
                self.turnSpeed = self.joystick.getX() / 1.75
            elif (self.driveController.y() and self.joystick.getX() < 0):
                self.turnSpeed = self.joystick.getX() / 1.75
            elif (self.driveController.y() and self.driveController.left_trigger()):
                self.driveSpeed = (self.joystick.getRawAxis(2) * -1) / 1.75 
            elif (self.driveController.y() and self.driveController.right_trigger()):
                self.driveSpeed = self.joystick.getRawAxis(3) / 1.75
            elif (self.driveController.left_trigger()):
                self.driveSpeed = self.joystick.getRawAxis(2) * -0.8
                self.turnSpeed = 0
            elif (self.driveController.right_trigger()):
                self.driveSpeed = self.joystick.getRawAxis(3) * 0.8
                self.turnSpeed = 0
            else:
                self.driveSpeed = 0
                self.ramp.stopLeft()
                self.turnSpeed = self.joystick.getX() * 0.8
            
            self.drivetrain.arcadeDrive(self.driveSpeed, self.turnSpeed)
