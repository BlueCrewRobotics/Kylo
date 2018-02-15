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

        # Create Motors
        self.left = wpilib.VictorSP(0)
        self.right = wpilib.VictorSP(1)

        # Create Differential Drive (Entire Drive Train)
        self.drive = wpilib.drive.DifferentialDrive(self.left, self.right)

        # Intake Motors
        self.intakeMotor = wpilib.VictorSP(2)

        # Intake Lifter
        self.intakeLifter = wpilib.Spark(6)

        # Create Shifter Pneumatics
        self.shifter = wpilib.DoubleSolenoid(0, 0, 1)
        
        # Create Drive Joystick
        self.driveStick = wpilib.Joystick(0)

        # Create Controller for Driving
        self.driveController = XboxController(0)

        # Create Controller for Subsystem Control
        self.subsystemController = XboxController(1)
        
        # Create Timer (For Making Timed Events)
        self.timer = wpilib.Timer()

        # Robot Drive Speed (Determined by Triggers in teleopPeriodic Function)
        self.driveSpeed = 0

        # Shifter State (To Allow Simple Automatic Shifting)
        self.shiftState = 0 

        # Initialize Driver Station
        self.driverStation = wpilib.DriverStation.getInstance()

        # Initialize Accelerometer
        self.accel = wpilib.builtinaccelerometer.BuiltInAccelerometer()

        # Initialize Sendable Chooser for Auto
        self.autoChooser = wpilib.SendableChooser()

        # Add Items to Auto Chooser
        self.autoChooser.addDefault('Center', 'C')
        self.autoChooser.addObject('Left', 'L')
        self.autoChooser.addObject('Right', 'R')
        self.autoChooser.addObject('Move Forward', 'MF')
        self.autoChooser.addObject('Do Not Move', 'DNM')

        # Put Auto Chooser on SmartDashboard
        wpilib.SmartDashboard.putData('Auto Mode', self.autoChooser)

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

        # Reset NavX
        self.navx.reset()

        # Variable to See if Robot Has Completed Turn
        self.hasCompletedTurn = False

        # Auto Stage Variable
        self.autoStage = 0

    # Called Periodically During Auto
    def autonomousPeriodic(self):

        # ---- Game Data Detection ---- 
        # code for detecting the side of
        # the switch we need to use
        if (self.gameData == "L"):
            if (self.autoMode == "L"):
                self.LeftStationLeftSwitch()
            elif (self.autoMode == "C"):
                self.CenterStationLeftSwitch()
            elif (self.autoMode == "R"):
                self.RightStationLeftSwitch()
            elif (self.autoMode == "MF"):
                self.EmergencyAuto()
            elif (self.autoMode == "DNM"):
                self.DoNotMove()
            else:
                self.EmergencyAuto()
        elif (self.gameData == "R"):
            if (self.autoMode == "L"):
                self.LeftStationRightSwitch()
            elif (self.autoMode == "C"):
                self.CenterStationRightSwitch()
            elif (self.autoMode == "R"):
                self.RightStationRightSwitch()
            elif (self.autoMode == "MF"):
                self.EmergencyAuto()
            elif (self.autoMode == "DNM"):
                self.DoNotMove()
            else:
                self.EmergencyAuto()
        else:
            self.EmergencyAuto()
            
    def teleopInit(self):

        # Reset Timer
        self.timer.reset()

        # Start Timer
        self.timer.start()

    # Called Periodically During Teleop
    def teleopPeriodic(self):

        # Create Arcade Drive Instance
        self.drive.arcadeDrive(self.driveSpeed, (self.driveStick.getX() * -1))

        # Get DPad Button
        dpadButton = self.subsystemController.dpad()

        # Rumble Controller
        if (self.timer.get() > 110 and self.timer.get() < 120):
            self.driveController.rumble(1, 1)
        else:
            self.driveController.rumble(0, 0)
        
        # Automatically Shift on Right Bumper Pressed
        if (self.driveController.right_bumper()):
            if (self.shiftState == 0):
                self.shifter.set(1)
                self.shiftState = 1
                self.timer.delay(0.5)
            elif (self.shiftState == 1):
                self.shifter.set(2)
                self.shiftState = 0
                self.timer.delay(0.5)

        # Drive Forward with Right Trigger
        elif (self.driveController.right_trigger()):
            self.driveSpeed = self.driveStick.getRawAxis(3)

        # Drive Backwards with Left Trigger
        elif (self.driveController.left_trigger()):
            self.driveSpeed = self.driveStick.getRawAxis(2) * -1

        # Intake on Right Bumper Pressed
        elif (self.subsystemController.right_bumper()):
            self.intakeMotor.set(0.5)

        # Push Out on Left Bumper Pressed
        elif (self.subsystemController.left_bumper()):
            self.intakeMotor.set(-0.75)

        # Intake on Right Trigger Pressed
        elif (self.subsystemController.right_trigger()):
            self.intakeLifter.set(0.5)

        # Push Out on Left Trigger Pressed
        elif (self.subsystemController.left_trigger()):
            self.intakeLifter.set(-0.3)

        # Push up Right Ramp on DPad Right Pressed
        elif (self.subsystemController.a() and dpadButton != -1 and dpadButton > 0 and dpadButton < 180):
            print("RIGHT")

        # Push up Right Ramp on DPad Left Pressed
        elif (self.subsystemController.a() and dpadButton != -1 and dpadButton > 180 and dpadButton < 359):
            print("Left")

        # Set All Motors to Stop
        else:
            self.intakeMotor.set(0)
            self.intakeLifter.set(0)
            self.shifter.set(0)
            self.driveSpeed = 0


    def LeftStationLeftSwitch(self):
        if (self.autoStage == 0):
            if (self.timer.get() < 2.34696):
                self.drive.arcadeDrive(-0.75, 0.275)
            else:
                self.autoStage += 1

        elif (self.autoStage == 1):
            turn = self.turnToAngle(90, "R")
            if (turn == True):
                self.autoStage += 1

        elif (self.autoStage == 2):
            if (self.timer.get() > 5 and self.timer.get() < 5.70):
                self.drive.arcadeDrive(-0.75, 0.275)
            elif (self.timer.get() > 5.56):
                self.autoStage += 1
                self.drive.arcadeDrive(0, 0)

        elif (self.autoStage == 3):
            print("TIME TO SHOOT")


    def LeftStationRightSwitch(self):
        if (self.autoStage == 0):
            if (self.timer.get() < 3.192145):
                self.drive.arcadeDrive(-0.75, 0.275)
            else:
                self.autoStage += 1

        elif (self.autoStage == 1):
            turn = self.turnToAngle(90, "R")
            if (turn == True):
                self.autoStage += 1

        elif (self.autoStage == 2):
            if (self.timer.get() > 6 and self.timer.get() < 8.95640125):
                self.drive.arcadeDrive(-0.75, 0.275)
            elif (self.timer.get() > 8.95640126):
                self.autoStage += 1
                self.drive.arcadeDrive(0, 0)

        elif (self.autoStage == 3):
            turn = self.turnToAngle(0, "R")
            if (turn == True):
                self.autoStage += 1

        elif (self.autoStage == 4):
            if (self.timer.get() > 10 and self.timer.get() < 10.25):
                self.drive.arcadeDrive(-0.75, 0.275)     
            elif (self.timer.get() > 10.26):
                self.autoStage += 1
                self.drive.arcadeDrive(0, 0)

        elif (self.autoStage == 5):
            print("TIME TO SHOOT")


    def CenterStationLeftSwitch(self):
        if (self.autoStage == 0):
            if (self.timer.get() < 0.185):
                self.drive.arcadeDrive(-0.75, 0.275)
            else:
                self.autoStage += 1

        elif (self.autoStage == 1):
            turn = self.turnToAngle(40, "L")
            if (turn == True):
                self.autoStage += 1

        elif (self.autoStage == 2):
            if (self.timer.get() > 3 and self.timer.get() < 3.70):
                self.drive.arcadeDrive(-0.75, 0.275)
            elif (self.timer.get() > 3.56):
                self.autoStage += 1
                self.drive.arcadeDrive(0, 0)

        elif (self.autoStage == 3):
            turn = self.turnToAngle(0, "R")
            if (turn == True):
                self.autoStage += 1

        elif (self.autoStage == 4):
            if (self.timer.get() > 6 and self.timer.get() < 6.25):
                self.drive.arcadeDrive(-0.75, 0.275)
            elif (self.timer.get() > 6.26):
                self.autoStage += 1
                self.drive.arcadeDrive(0, 0)

        elif (self.autoStage == 5):
            print("TIME TO SHOOT")


    def CenterStationRightSwitch(self):
        if (self.autoStage == 0):
            if (self.timer.get() < 0.185):
                self.drive.arcadeDrive(-0.75, 0.275)
            else:
                self.autoStage += 1

        elif (self.autoStage == 1):
            turn = self.turnToAngle(40, "R")
            if (turn == True):
                self.autoStage += 1

        elif (self.autoStage == 2):
            if (self.timer.get() > 3 and self.timer.get() < 3.70):
                self.drive.arcadeDrive(-0.75, 0.275)
            elif (self.timer.get() > 3.56):
                self.autoStage += 1
                self.drive.arcadeDrive(0, 0)

        elif (self.autoStage == 3):
            turn = self.turnToAngle(0, "L")
            if (turn == True):
                self.autoStage += 1

        elif (self.autoStage == 4):
            if (self.timer.get() > 6 and self.timer.get() < 6.25):
                self.drive.arcadeDrive(-0.75, 0.275)
            elif (self.timer.get() > 6.26):
                self.autoStage += 1
                self.drive.arcadeDrive(0, 0)

        elif (self.autoStage == 5):
            print("TIME TO SHOOT")


    def RightStationLeftSwitch(self):
        if (self.autoStage == 0):
            if (self.timer.get() < 3.192145):
                self.drive.arcadeDrive(-0.75, 0.275)
            else:
                self.autoStage += 1

        elif (self.autoStage == 1):
            turn = self.turnToAngle(90, "L")
            if (turn == True):
                self.autoStage += 1

        elif (self.autoStage == 2):
            if (self.timer.get() > 6 and self.timer.get() < 8.95640125):
                self.drive.arcadeDrive(-0.75, 0.275)
            elif (self.timer.get() > 8.95640126):
                self.autoStage += 1
                self.drive.arcadeDrive(0, 0)

        elif (self.autoStage == 3):
            turn = self.turnToAngle(0, "L")
            if (turn == True):
                self.autoStage += 1

        elif (self.autoStage == 4):
            if (self.timer.get() > 10 and self.timer.get() < 10.25):
                self.drive.arcadeDrive(-0.75, 0.275)
            elif (self.timer.get() > 10.26):
                self.autoStage += 1
                self.drive.arcadeDrive(0, 0)

        elif (self.autoStage == 5):
            print("TIME TO SHOOT")


    def RightStationRightSwitch(self):
        if (self.autoStage == 0):
            if (self.timer.get() < 2.34696):
                self.drive.arcadeDrive(-0.75, 0.275)
            else:
                self.autoStage += 1

        elif (self.autoStage == 1):
            turn = self.turnToAngle(90, "L")
            if (turn == True):
                self.autoStage += 1

        elif (self.autoStage == 2):
            if (self.timer.get() > 5 and self.timer.get() < 5.70):
                self.drive.arcadeDrive(-0.75, 0.275)
            elif (self.timer.get() > 5.56):
                self.autoStage += 1
                self.drive.arcadeDrive(0, 0)

        elif (self.autoStage == 3):
            print("TIME TO SHOOT")


    def EmergencyAuto(self):
        if (self.timer.get() < 2.72415):
            self.drive.arcadeDrive(-0.75, 0.275)
        else:
            self.drive.arcadeDrive(0, 0)


    def DoNotMove(self):
        pass
       
            
    def turnToAngle(self, angle, direction):
        # Turn 90 Degrees Code

        if (self.hasCompletedTurn == True):
            self.hasCompletedTurn = False
            self.turnState = True

        # While Not at 90 Degrees, Keep Turning
        if(self.turnState == True):
            # Turn to Range of Degrees
            if (direction == "R"):
                if (self.navx.getYaw() > angle):
                    # Stop Driving
                    self.drive.arcadeDrive(0, 0)
                    # Tell the Robot that it's Done Turning
                    self.turnState = False
                    self.hasCompletedTurn = True
                    return True
                else:
                    # Turn the Robot
                    self.drive.arcadeDrive(0, 0.4)
                    self.turnState = True
            elif (direction == "L"):
                if (self.navx.getYaw() < angle * -1):
                    # Stop Driving
                    self.drive.arcadeDrive(0, 0)
                    # Tell the Robot that it's Done Turning
                    self.turnState = False
                    self.hasCompletedTurn = True
                    return True
                else:
                    # Turn the Robot
                    self.drive.arcadeDrive(0, -0.4)
                    self.turnState = True
    
    def driveDistance(self, travelDistance):

        # Get Acceleration
        accel = self.accel.getY()

        if (self.hasMovedDistance == False):

            self.drive.arcadeDrive(-0.45, 0.275)

            # Get Time Delta
            #timeDelta = 0.5
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
            #print(round(accel, 2))

            if (sum(self.distances) <= travelDistance):
                self.hasMovedDistance = True
                self.drive.arcadeDrive(0, 0)
                self.distances = []
                self.initialAcceleration = []
                return True

# Run Main Robot Code Loop
if __name__ == "__main__":
    wpilib.run(Kylo)