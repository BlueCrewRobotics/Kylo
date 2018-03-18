'''

 -- Drive Train --

Blue Crew Robotics Team 6153
Authors: Matthew Gallant, Jacob Mealey

'''

import wpilib
import wpilib.drive

from networktables import NetworkTables

from robotpy_ext.common_drivers import navx

class DriveTrain:

    robotDrive = wpilib.drive.DifferentialDrive
    driveJoystick = wpilib.Joystick
    rightDrive = wpilib.VictorSP
    leftDrive = wpilib.VictorSP

    navX = navx.AHRS

    accel = wpilib.BuiltInAccelerometer
    
    shifterSolenoid = wpilib.DoubleSolenoid

    timer = wpilib.Timer

    shiftState = False

    hasCompletedTurn = False
    turnState = True

    navXState = False

    hasMovedDistance = False
    autoDistanceTiming = 0
    initialAcceleration = []
    distances = []

    sd = NetworkTables.getTable('SmartDashboard')

    def arcadeDrive(self, ySpeed, xSpeed):    
        self.robotDrive.arcadeDrive(ySpeed, (xSpeed * -1), True)
    
    def driveStraight(self):        
        self.robotDrive.arcadeDrive(0.75, 0.4)

    def stopDrive(self):
        self.robotDrive.arcadeDrive(0, 0)
    
    def shiftGear(self):
        if (self.shiftState == False):
            self.shifterSolenoid.set(1)
            self.shiftState = True
            self.sd.putString("Shift State", "Low Gear")
        elif (self.shiftState == True):
            self.shifterSolenoid.set(2)
            self.shiftState = False
            self.sd.putString("Shift State", "High Gear")

    def turnToAngleRight(self, angle):

        if (self.navXState == False):
            self.navX.reset()
            self.navXState = True

        # While Not at 90 Degrees, Keep Turning
        if(self.turnState == True):
            # Turn to Range of Degrees
            print(self.navX.getYaw())
            if (self.navX.getYaw() < angle * -1):
                # Stop Driving
                self.robotDrive.arcadeDrive(0, 0)
                # Tell the Robot that it's Done Turning
                self.turnState = False
                self.navX.reset()
                self.hasCompletedTurn = True
                return True
            else:
                # Turn the Robot
                self.robotDrive.arcadeDrive(0, 0.75)
                self.turnState = True

    def turnToAngleLeft(self, angle):

        if (self.navXState == False):
            self.navX.reset()
            self.navXState = True

        # While Not at 90 Degrees, Keep Turning
        if(self.turnState == True):
            print(self.navX.getYaw())
            if (self.navX.getYaw() > angle):
                # Stop Driving
                self.robotDrive.arcadeDrive(0, 0)
                # Tell the Robot that it's Done Turning
                self.turnState = False
                self.navX.reset()
                self.hasCompletedTurn = True
                return True
            else:
                # Turn the Robot
                self.robotDrive.arcadeDrive(0, -0.75)
                self.turnState = True

    def resetNavX(self):
        self.navXState = False
        self.turnState = True
    
    def driveDistance(self, travelDistance):

        # Get Acceleration
        accel = self.accel.getY()

        if (self.hasMovedDistance == False):

            self.robotDrive.arcadeDrive(-0.45, 0.275)

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
                self.robotDrive.arcadeDrive(0, 0)
                self.distances = []
                self.initialAcceleration = []
                return True

    def execute(self):
        pass