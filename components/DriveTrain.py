'''

Drive Mechanisms

'''

import wpilib
import wpilib.drive

class DriveTrain:

    robotDrive = wpilib.drive.DifferentialDrive
    driveJoystick = wpilib.Joystick
    rightDrive = wpilib.VictorSP
    leftDrive = wpilib.VictorSP
    
    shifterSolenoid = wpilib.DoubleSolenoid

    timer = wpilib.Timer

    shiftState = False

    def arcadeDrive(self, speed):        
        self.robotDrive.arcadeDrive(speed, (self.driveJoystick.getX() * -1))
    
    def driveStraight(self):        
        self.robotDrive.arcadeDrive(0.75, 0.25)
    
    def shiftGear(self):
        if (self.shiftState == False):
            self.shifterSolenoid.set(1)
            self.shiftState = True
            self.timer.delay(0.5)
        elif (self.shiftState == True):
            self.shifterSolenoid.set(2)
            self.shiftState = False
            self.timer.delay(0.5)

    def execute(self):
        pass