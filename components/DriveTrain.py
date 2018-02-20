'''

Drive Mechanisms

'''

import wpilib
import wpilib.drive

from robotpy_ext.common_drivers import navx

class DriveTrain:

    robotDrive = wpilib.drive.DifferentialDrive
    driveJoystick = wpilib.Joystick
    rightDrive = wpilib.VictorSP
    leftDrive = wpilib.VictorSP

    navx = navx.AHRS.create_spi()
    
    shifterSolenoid = wpilib.DoubleSolenoid

    timer = wpilib.Timer

    shiftState = False

    hasCompletedTurn = False
    turnState = True

    hasMovedDistance = False
    autoDistanceTiming = 0
    initialAcceleration = []
    distances = []

    def arcadeDrive(self, speed):        
        self.robotDrive.arcadeDrive(speed / 1.25, (self.driveJoystick.getX() * -1) / 1.25)
    
    def driveStraight(self):        
        self.robotDrive.arcadeDrive(0.75, 0.25)
    
    def shiftGear(self):
        if (self.shiftState == False):
            self.shifterSolenoid.set(1)
            self.shiftState = True
        elif (self.shiftState == True):
            self.shifterSolenoid.set(2)
            self.shiftState = False

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
                    self.robotDrive.arcadeDrive(0, 0)
                    # Tell the Robot that it's Done Turning
                    self.turnState = False
                    self.hasCompletedTurn = True
                    return True
                else:
                    # Turn the Robot
                    self.robotDrive.arcadeDrive(0, 0.4)
                    self.turnState = True
            elif (direction == "L"):
                if (self.navx.getYaw() < angle * -1):
                    # Stop Driving
                    self.robotDrive.arcadeDrive(0, 0)
                    # Tell the Robot that it's Done Turning
                    self.turnState = False
                    self.hasCompletedTurn = True
                    return True
                else:
                    # Turn the Robot
                    self.robotDrive.arcadeDrive(0, -0.4)
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