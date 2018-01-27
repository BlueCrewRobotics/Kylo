#!/usr/bin/env python3

"""
    Blue Crew 2018 Robot Code
    Codename: Kylo
"""

import wpilib
import wpilib.drive

from robotpy_ext.common_drivers import navx
from networktables import NetworkTables
from xbox import XboxController

class Kylo(wpilib.IterativeRobot):

    # Initialize All of the Components
    def robotInit(self):

        #Initialize NetworkTable for new SmartDashboard
        self.sd = NetworkTables.getTable("SmartDashboard")

        #Initialize NavX on SPI bus
        self.navx = navx.AHRS.create_spi()

        # Left Motors
        self.left_front = wpilib.VictorSP(0)
        self.left_rear = wpilib.VictorSP(1)
        self.left = wpilib.SpeedControllerGroup(self.left_front, self.left_rear)

        # Right Motors
        self.right_front = wpilib.VictorSP(2)
        self.right_rear = wpilib.VictorSP(3)
        self.right = wpilib.SpeedControllerGroup(self.right_front, self.right_rear)

        # Create Differential Drive (Entire Drive Train)
        self.drive = wpilib.drive.DifferentialDrive(self.left, self.right)

        # Intake Motors
        self.intake_one = wpilib.VictorSP(4)
        self.intake_two = wpilib.VictorSP(5)

        # Create Shifter Pneumatics
        self.shifter = wpilib.DoubleSolenoid(0, 2, 0)
        
        # Create Joystick
        self.stick = wpilib.Joystick(0)

        # Create Controller for Buttons
        self.controller = XboxController(0)
        
        # Create Timer (For Making Timed Events)
        self.timer = wpilib.Timer()

    # Called Each Time the Robot Runs Auto Mode
    def autonomousInit(self):
        
        # Reset Timer
        self.timer.reset()

        self.sd.putNumber("numbers", 1)
        # Start Timer
        self.timer.start()

    # Called Periodically During Auto
    def autonomousPeriodic(self):

        # Drive for Two Seconds
        if self.timer.get() < 2.0:
            # Drive Forwards at Half Speed
            self.drive.arcadeDrive(-0.5, 0)
        else:
            # Stop Robot
            self.drive.arcadeDrive(0, 0)

    # Called Periodically During Teleop
    def teleopPeriodic(self):

     
        # Create Arcade Drive Instance
        self.drive.arcadeDrive(self.stick.getY() / 2, self.stick.getX() / 2)
        
        # Shift Up on Button Right Bumber Pressed
        if (self.controller.right_bumper()):
            self.shifter.set(2)
            print(self.shifter.get())
        # Shift Down on Button Left Bumper Pressed
        elif (self.controller.left_bumper()):
            self.shifter.set(1)
            print(self.shifter.get())
        # Intake on Button A Pressed
        elif (self.controller.a()):
            self.intake_one.set(0.5)
            self.intake_two.set(0.5)
        # Push Out on Button B Pressed
        elif (self.controller.b()):
            self.intake_one.set(-0.5)
            self.intake_two.set(-0.5)
        # Set All Motors to Stop
        else:
            self.intake_one.set(0)
            self.intake_two.set(0)
            self.shifter.set(0)
        
        
        self.sd.putNumber('Yaw', self.navx.getYaw())




# Run Main Robot Code Loop
if __name__ == "__main__":

    wpilib.run(Kylo)