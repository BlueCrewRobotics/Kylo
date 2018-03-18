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
        self.summedSpeed = 0

    def run(self):

        while True:

            time.sleep(self.delay)

            self.summedSpeed = self.joystick.getRawAxis(2) * -0.8 + self.joystick.getRawAxis(3) * 0.8
            
            if (self.joystick.getX() > 0.1 or self.joystick.getX() < -0.1 or self.summedSpeed > 0.1 or self.summedSpeed < -0.1):
                
                if (self.summedSpeed > 0.1):
                    self.driveSpeed = (self.summedSpeed) * 0.7 + 0.3
                elif (self.summedSpeed < -0.1):
                    self.driveSpeed = (self.summedSpeed) * 0.7 + -0.3
                else:
                    self.driveSpeed = 0
                
                if (self.joystick.getX() > 0.1):
                    self.turnSpeed = (self.joystick.getX() * 0.6) * 0.7 + 0.3
                elif (self.joystick.getX() < -0.1):
                    self.turnSpeed = (self.joystick.getX() * 0.6) * 0.7 + -0.3
                else:
                    self.turnSpeed = 0
                
            else:
                self.driveSpeed = 0
                self.turnSpeed = 0
                self.summedSpeed = 0
            
            self.drivetrain.arcadeDrive(self.driveSpeed, self.turnSpeed)
