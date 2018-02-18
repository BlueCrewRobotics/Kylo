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
        self.rightRamp.set(0.75)

    def raiseLeftRamp(self):
        self.leftRamp.set(0.75)
    
    def lowerRightRamp(self):
        self.rightRamp.set(-0.75)

    def lowerLeftRamp(self):
        self.leftRamp.set(-0.75)

    def deployRamps(self):
        if (self.rampState == False):
            self.rampSolenoid.set(True)
            self.rampState = True
            self.timer.delay(0.5)
        elif (self.rampState == True):
            self.rampSolenoid.set(False)
            self.rampState = False
            self.timer.delay(0.5)

    def execute(self):
        pass