#!/usr/bin/env python3

'''
    Blue Crew Robot Code for FIRST Power Up
    Codename: Kylo
'''

import wpilib
import wpilib.drive

from wpilib.buttons import JoystickButton
from magicbot import MagicRobot

from components.DriveTrain import DriveTrain
from components.CubeMech import CubeMech
from components.RampMech import RampMech

from common.xbox import XboxController

class Kylo(MagicRobot):
    
    # Initialize Robot Components
    drivetrain = DriveTrain
    cubemech = CubeMech
    rampmech = RampMech

    def createObjects(self):

        # Define Driving Motors
        self.rightDrive = wpilib.VictorSP(1)
        self.leftDrive = wpilib.VictorSP(0)

        # Create Robot Drive
        self.robotDrive = wpilib.drive.DifferentialDrive(self.rightDrive, self.leftDrive)

        # Create Shifter Pneumatics
        self.shifterSolenoid = wpilib.DoubleSolenoid(0, 0, 1)

        # Joysticks and Controllers
        self.driveJoystick = wpilib.Joystick(0)
        self.driveController = XboxController(0)
        
        self.subsystemJoystick = wpilib.Joystick(1)
        self.subsystemController = XboxController(1)

        # Set Drivespeed
        self.driveSpeed = 0

        # Intake Motors
        self.intakeMotor = wpilib.VictorSP(2)

        # Intake Lifter
        self.intakeLifter = wpilib.Spark(6)

        # Create Cube Intake Pneumatics
        self.intakeSolenoid = wpilib.Solenoid(0, 2)

        # Create Ramp Motors
        self.rightRamp = wpilib.Spark(5)
        self.leftRamp = wpilib.Spark(4)

        # Create Ramp Deploy Pneumatics
        self.rampSolenoid = wpilib.Solenoid(0, 3)

        # Create Timer (For Making Timed Events)
        self.timer = wpilib.Timer()

    def teleopPeriodic(self):

        # --------- Start Drive Commands ----------

        self.drivetrain.arcadeDrive(self.driveSpeed)

        if (self.driveController.right_trigger()):
            self.driveSpeed = self.driveJoystick.getRawAxis(3)
        else:
            self.driveSpeed = 0

        if (self.driveController.left_trigger()):
            self.driveSpeed = self.driveJoystick.getRawAxis(2) * -1
        else:
            self.driveSpeed = 0

        if (self.driveController.right_bumper()):
            self.drivetrain.shiftGear()
        
        # --------- End Drive Commands ----------

        # --------- Start Cube Commands ----------

        if (self.subsystemController.b()):
            self.cubemech.clampCube()

        if (self.subsystemController.right_trigger()):
            self.cubemech.liftArm()

        if (self.subsystemController.left_trigger()):
            self.cubemech.lowerArm()

        if (self.subsystemController.right_bumper()):
            self.cubemech.intakeCube()

        if (self.subsystemController.left_bumper()):
            self.cubemech.shootCube()

        # --------- End Cube Commands ----------

        # --------- Start Ramp Commands ----------

        if (self.subsystemController.a() and self.subsystemController.y()):
            self.rampmech.deployRamps()

        if (self.subsystemController.a() and self.subsystemController.x()):
            self.rampmech.raiseRightRamp()

        if (self.subsystemController.a() and self.subsystemController.b()):
            self.rampmech.lowerRightRamp()

        if (self.driveController.a() and self.driveController.x()):
            self.rampmech.raiseLeftRamp()

        if (self.driveController.a() and self.driveController.b()):
            self.rampmech.lowerLeftRamp()

        # --------- End Ramp Commands ----------

if __name__ == '__main__':
    wpilib.run(Kylo)