#!/usr/bin/env python3

"""
    Blue Crew 2018 Robot Code
    Codename: Kylo
"""

# Main Imports
import wpilib
import wpilib.drive

# Extra Imports
from robotpy_ext.common_drivers import navx
from networktables import NetworkTables

# Project Only Imports
from xbox import XboxController

# Begin Robot Code
class Kylo(wpilib.IterativeRobot):

    # Initialize All of the Components
    def robotInit(self):

        # Initialize NetworkTable for new SmartDashboard
        self.sd = NetworkTables.getTable("SmartDashboard")

        # Initialize NavX on SPI bus
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

        # Robot Drive Speed (Determined by Triggers in teleopPeriodic Function)
        self.driveSpeed = 0

        # Shifter State (To Allow Simple Automatic Shifting)
        self.shiftState = 0 

        # Initialize Driver Station
        self.driverStation = wpilib.DriverStation.getInstance()

        # Create Variable for Auto Distance Measurement
        self.autoDistanceTiming = 0

        # Initialize Accelerometer
        self.accel = wpilib.builtinaccelerometer.BuiltInAccelerometer()

        # Initialize Sendable Chooser for Auto
        self.autoChooser = wpilib.SendableChooser()

        # Add Items to Auto Chooser
        self.autoChooser.addObject('Left', 'L')
        self.autoChooser.addDefault('Center', 'C')
        self.autoChooser.addObject('Right', 'R')

        # Put Auto Chooser on SmartDashboard
        wpilib.SmartDashboard.putData('Auto Positon', self.autoChooser)

    # Called Each Time the Robot Runs Auto Mode
    def autonomousInit(self):
        
        # Reset Timer
        self.timer.reset()

        # Start Timer
        self.timer.start()

        # Set Turn State
        self.turnState = True

        # Get Switch Position (L or R)
        try:
            self.gameData = self.driverStation.getGameSpecificMessage()[0]
        except IndexError:
            self.gameData = "UNKNOWN"

        # Initial Acceleration Arrray
        self.initialAcceleration = []

        # Distance Calculations Array
        self.distances = []

        # Set Auto Distance Timing Variable
        self.autoDistanceTiming = self.timer.getMsClock()

        # Set True if Distance Traveled is Complete
        self.hasMovedDistance = False

        # Get Auto Mode from Chooser
        self.autoMode = self.autoChooser.getSelected()
        print(self.autoMode)
        

    # Called Periodically During Auto
    def autonomousPeriodic(self):

        '''

        # Turn 90 Degrees Code

        # Reset NavX
        self.navx.reset()

        # While Not at 90 Degrees, Keep Turning
        while(self.turnState == True):
            # Turn to Range of Degrees
            if (85.5 < self.navx.getYaw() < 90):
                # Stop Driving
                self.drive.arcadeDrive(0, 0)

                # Tell the Robot that it's Done Turning
                self.turnState = False
                break
            else:
                # Turn the Robot
                self.drive.arcadeDrive(0, 0.4)

        '''

        '''

        # Measure Distance Code

        # Get Acceleration
        accel = self.accel.getY()

        if (self.hasMovedDistance == False):
            self.drive.arcadeDrive(0.55, 0)

            # Get Time Delta
            timeDelta = (self.timer.getMsClock() - self.autoDistanceTiming) / 1000
            
            # Reset Distance Timing
            self.autoDistanceTiming = self.timer.getMsClock()

            # Send Initial Acceleration to Array
            self.initialAcceleration.append((round(accel, 2) * 9.8) * timeDelta)

            # Get Velocity
            velocity = sum(self.initialAcceleration)

            # Get Distance
            distance = velocity * timeDelta

            # Send Distace to Array
            self.distances.append(distance)

            print("Total Distance: " + str(sum(self.distances)))

            if (sum(self.distances) <= -1.5):
                self.hasMovedDistance = True
                self.drive.arcadeDrive(0, 0)
        '''

        '''

        # Code for Getting Switch Data

        # Run for Two Seconds
        if self.timer.get() < 2.0:
            # Determine is Switch is on the Right or Left
            if (self.gameData == "L"):
                print("Left Switch")
            elif (self.gameData == "R"):
                print("Right Switch")
            else:
                # Report Error to Driver Station
                self.driverStation.reportError("Could Not Detect Switch Position! Quiting Auto Mode!", False)
        else:
            # Stop Robot
            self.drive.arcadeDrive(0, 0)
        '''

    # Called Periodically During Teleop
    def teleopPeriodic(self):

        # Create Arcade Drive Instance
        self.drive.arcadeDrive(self.driveSpeed, self.stick.getX() / 2)
        
        # Automatically Shift on Right Bumper Pressed
        if (self.controller.right_bumper()):
            if (self.shiftState == 0):
                self.shifter.set(1)
                self.shiftState = 1
                self.timer.delay(0.5)
            elif (self.shiftState == 1):
                self.shifter.set(2)
                self.shiftState = 0
                self.timer.delay(0.5)
        # Drive Forward with Right Trigger
        elif (self.controller.right_trigger()):
            self.driveSpeed = self.stick.getRawAxis(3)
        # Drive Backwards with Left Trigger
        elif (self.controller.left_trigger()):
            self.driveSpeed = self.stick.getRawAxis(2) * -1
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
            self.driveSpeed = 0

# Run Main Robot Code Loop
if __name__ == "__main__":
    wpilib.run(Kylo)