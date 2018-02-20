#!/usr/bin/env python3

'''
    Blue Crew Robot Code for FIRST Power Up
    Codename: Kylo
'''

import wpilib
import wpilib.drive
import threading

from wpilib.buttons import JoystickButton
from magicbot import MagicRobot

from components.DriveTrain import DriveTrain
from components.CubeMech import CubeMech
from components.RampMech import RampMech

from common.driveController import driveController
from common.subsystemController import subsystemController
from common.xbox import XboxController

class Kylo(MagicRobot):
    
    # Initialize Robot Components
    drivetrain = DriveTrain
    cubemech = CubeMech
    rampmech = RampMech

    def createObjects(self):

        # Define Driving Motors
        self.rightDrive = wpilib.VictorSP(0)
        self.leftDrive = wpilib.VictorSP(1)

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
        self.intakeMotor = wpilib.VictorSP(9)

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

        # Initialize Compressor
        self.compressor = wpilib.Compressor()

        # Create CameraServer
        wpilib.CameraServer.launch("common/multipleCameras.py:main")

        # Set Gear in Dashboard
        wpilib.SmartDashboard.putString("Shift State", "Low Gear")
        wpilib.SmartDashboard.putString("Cube State", "Unclamped")

    def teleopInit(self):
        DriverController = driveController("DriveController", self.driveController, self.drivetrain, self.cubemech, self.rampmech, self.driveJoystick, .05)
        SubsystemController = subsystemController("SubsystemController", self.subsystemController, self.driveJoystick, self.cubemech, self.rampmech, .1)
        
        DriverController.start()
        SubsystemController.start()
        
        self.timer.reset()
        self.timer.start()

    def teleopPeriodic(self):
        # Rumble Controller
        if (self.timer.get() > 110 and self.timer.get() < 120):
            self.driveController.rumble(1, 1)
        else:
            self.driveController.rumble(0, 0)

if __name__ == '__main__':
    wpilib.run(Kylo)