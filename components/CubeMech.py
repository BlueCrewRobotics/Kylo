'''

Cube Mechanisms

'''

import wpilib

class CubeMech:

    intakeMotor = wpilib.VictorSP
    intakeLifter = wpilib.Spark
    
    intakeSolenoid = wpilib.Solenoid

    compressor = wpilib.Compressor

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
        elif (self.intakeState == True):
            self.intakeSolenoid.set(False)
            self.intakeState = False

    def startPressurize(self):
        self.compressor.start()

    def stopPressurize(self):
        self.compressor.stop()

    def execute(self):
        pass