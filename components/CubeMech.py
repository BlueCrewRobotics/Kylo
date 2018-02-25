'''

 -- Cube Mechanisms --
 
Blue Crew Robotics Team 6153
Authors: Matthew Gallant, Jacob Mealey

'''

import wpilib
from components.BinaryPneumatic import BinaryPneuamtic

class CubeMech:

    intakeMotor = wpilib.VictorSP
    intakeLifter = wpilib.Spark
    
    intakeSolenoid = wpilib.Solenoid

    compressor = wpilib.Compressor

    timer = wpilib.Timer

    intakeState = False

    pneumatics = BinaryPneuamtic(intakeSolenoid, "CubeMech")

    def liftArm(self):
        self.intakeLifter.set(-1.0)
    
    def lowerArm(self):
        self.intakeLifter.set(1.0)

    def shootCube(self):
        self.intakeMotor.set(-0.35)
    
    def intakeCube(self):
        self.intakeMotor.set(0.5)

    def stop(self):
        self.intakeMotor.set(0)
        self.intakeLifter.set(0)

    def clampCube(self):
        # if (self.intakeState == False):
        #     self.intakeSolenoid.set(True)
        #     self.intakeState = True
        #     wpilib.SmartDashboard.putString("Cube State", "Unclamped")
        # elif (self.intakeState == True):
        #     self.intakeSolenoid.set(False)
        #     self.intakeState = False
        #     wpilib.SmartDashboard.putString("Cube State", "Clamped")
        self.pneumatics.switch()

    def startPressurize(self):
        self.compressor.start()

    def stopPressurize(self):
        self.compressor.stop()

    def execute(self):
        pass