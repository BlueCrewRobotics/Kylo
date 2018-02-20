'''

Ramp Mechanisms

'''

import wpilib

class RampMech:

    rightRamp = wpilib.Spark
    leftRamp = wpilib.Spark
    
    rampSolenoid = wpilib.Solenoid

    timer = wpilib.Timer

    rampState = False

    def raiseRightRamp(self):
        self.rightRamp.set(0.85)

    def raiseLeftRamp(self):
        self.leftRamp.set(0.85)
    
    def lowerRightRamp(self):
        self.rightRamp.set(-0.75)

    def lowerLeftRamp(self):
        self.leftRamp.set(-0.75)
        
    def stopRight(self):
        self.rightRamp.set(0)

    def stopLeft(self):
        self.leftRamp.set(0)

    def deployRamps(self):
        if (self.rampState == False):
            self.rampSolenoid.set(True)
            self.rampState = True
        elif (self.rampState == True):
            self.rampSolenoid.set(False)
            self.rampState = False

    def execute(self):
        pass