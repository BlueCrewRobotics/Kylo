'''

Cube Mechanisms

'''

import wpilib

class CubeMech:

    intakeMotor = wpilib.VictorSP
    intakeLifter = wpilib.Spark
    
    intakeSolenoid = wpilib.Solenoid

    timer = wpilib.Timer

    intakeState = False

    def liftArm(self):
        self.intakeLifter.set(0.5)
    
    def lowerArm(self):
        self.intakeLifter.set(-0.3)

    def shootCube(self):
        self.intakeMotor.set(-0.75)
    
    def intakeCube(self):
        self.intakeMotor.set(0.5)

    def stop(self):
        self.intakeMotor.set(0)
        self.intakeLifter.set(0)

    def clampCube(self):
        if (self.intakeState == False):
            self.intakeSolenoid.set(True)
            self.intakeState = True
            self.timer.delay(0.5)
        elif (self.intakeState == True):
            self.intakeSolenoid.set(False)
            self.intakeState = False
            self.timer.delay(0.5)

    def execute(self):
        pass