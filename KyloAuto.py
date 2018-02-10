'''

Blue Crew Autonomous Functions

'''

import wpilib
from robotpy_ext.common_drivers import navx

class KyloAutonomous(object):

    # Initialize KyloAutonomous Class
    def __init__(self, driveTrain):
        # Set Drive Train
        self.drive = driveTrain
        
        # Initialize NavX on SPI Bus
        self.navx = navx.AHRS.create_spi()

        # Initialize Accelerometer (We Would Use the NavX Accelerometer, but it's Unreliable)
        self.accel = wpilib.builtinaccelerometer.BuiltInAccelerometer()

        # Create Timer (For Making Timed Events)
        self.timer = wpilib.Timer()

        # Initialize Driver Station
        self.driverStation = wpilib.DriverStation.getInstance()

        # Get Switch Position (L or R)
        try:
            self.gameData = self.driverStation.getGameSpecificMessage()[0]
        except IndexError:
            self.gameData = "UNKNOWN"

    # Determine Which Auto Mode to Run, and Run it
    def determineAuto(self, position):
        if (self.gameData == "L"):
            if (position == "L"):
                self.LeftStationLeftSwitch()
            elif (position == "C"):
                self.CenterStationLeftSwitch()
            elif (position == "R"):
                self.RightStationLeftSwitch()
            else:
                self.EmergencyAuto()
        elif (self.gameData == "R"):
            if (position == "L"):
                self.LeftStationRightSwitch()
            elif (position == "C"):
                self.CenterStationRightSwitch()
            elif (position == "R"):
                self.RightStationRightSwitch()
            else:
                self.EmergencyAuto()
        else:
            self.EmergencyAuto()

#=====================================================================================================
# Start Auto Modes
#=====================================================================================================

    def LeftStationLeftSwitch(self):
        print("LeftStationLeftSwitch")

    def LeftStationRightSwitch(self):
        print("LeftStationRightSwitch")

    def CenterStationLeftSwitch(self):
        print("CenterStationLeftSwitch")

    def CenterStationRightSwitch(self):
        print("CenterStationRightSwitch")

    def RightStationLeftSwitch(self):
        print("RightStationLeftSwitch")

    def RightStationRightSwitch(self):
        print("RightStationRightSwitch")

    def EmergencyAuto(self):
        print("EmergencyAuto")

#=====================================================================================================
# End Auto Modes
#=====================================================================================================

#=====================================================================================================
# Start Custom Functions
#=====================================================================================================

    # Function to Turn to Angle
    def turnToAngle(self, angle):

        # Initialize Turn State Variable
        turnState = True
        
        # Reset NavX
        self.navx.reset()

        # While Not at 90 Degrees, Keep Turning
        if(turnState == True):
            # Turn to Range of Degrees
            if (self.navx.getYaw() < angle):
                # Stop Driving
                self.drive.arcadeDrive(0, 0)
                # Tell the Robot that it's Done Turning
                turnState = False
            else:
                # Turn the Robot
                self.drive.arcadeDrive(0, 0.4)
    
    # Function to Move Forward to a Certain Distance
    def moveDistance(self, distance):

        # Initial Acceleration Arrray
        initialAcceleration = []

        # Distance Calculations Array
        distances = []
        
        # Set Auto Distance Timing Variable
        autoDistanceTiming = 0

        # Set True if Distance Traveled is Complete
        hasMovedDistance = False

        # Get Acceleration
        accel = self.accel.getY()

        # Check if Timer is Set
        if (autoDistanceTiming == 0):
            autoDistanceTiming = self.timer.getMsClock()

        # Find if Robot has Moved Distance
        if (hasMovedDistance == False):
            self.drive.arcadeDrive(0.55, 0)

            # Get Time Delta
            timeDelta = (self.timer.getMsClock() - autoDistanceTiming) / 1000
            
            # Reset Distance Timing
            autoDistanceTiming = self.timer.getMsClock()

            # Send Initial Acceleration to Array
            initialAcceleration.append((round(accel, 2) * 9.8) * timeDelta)

            # Get Velocity
            velocity = sum(initialAcceleration)

            # Get Distance
            distance = velocity * timeDelta

            # Send Distace to Array
            distances.append(distance)

            # Check if Robot Moved to Distance
            if (sum(distances) <= distance * -1):
                hasMovedDistance = True
                self.drive.arcadeDrive(0, 0)

#=====================================================================================================
# End Custom Functions
#=====================================================================================================
