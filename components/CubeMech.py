'''

 -- Cube Mechanisms --
 
Blue Crew Robotics Team 6153
Authors: Matthew Gallant, Jacob Mealey

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
        self.intakeSolenoid.set(True)

    def stopClampCube(self):
        self.intakeSolenoid.set(False)

    def startPressurize(self):
        self.compressor.start()

    def stopPressurize(self):
        self.compressor.stop()

    def execute(self):
        pass