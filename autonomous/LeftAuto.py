
import wpilib

from magicbot import AutonomousStateMachine, tunable, timed_state

from components.DriveTrain import DriveTrain
from components.CubeMech import CubeMech
                    
class Left(AutonomousStateMachine):

    MODE_NAME = 'Left'

    def __init__(self):

        self.drivetrain = DriveTrain
        self.cubemech = CubeMech

        self.driverStation = wpilib.DriverStation.getInstance()

        self.gameData = "U"

    @timed_state(duration=2.4, next_state='stateTwo', first=True)
    def stateOne(self):
        
        if (self.driverStation.getGameSpecificMessage()):
            # Try to Collect Switch Position Data
            try:
                self.gameData = self.driverStation.getGameSpecificMessage()[0]
            except IndexError:
                self.gameData = "UNKNOWN"

            # Print Switch Position (In event of failure for debugging)
            print("Auto Switch Position: " + self.gameData)

        # Pressurize Pneumatics
        self.cubemech.startPressurize()

        if (self.gameData == "L"):
            print("Entering Auto Mode: Left Position Left Switch")
        elif (self.gameData == "R"):
            print("Entering Auto Mode: Left Position Right Switch")
        else:
            print("Entering Auto Mode: Left Position Fail Safe")

    @timed_state(duration=2.0, next_state='stateThree')
    def stateTwo(self):
        # Pressurize Pneumatics
        self.cubemech.startPressurize()

        # Drive Forward
        print("Drive Forward")
        self.drivetrain.arcadeDrive(0.62, 0.20)

    @timed_state(duration=1.8, next_state='stateFour')
    def stateThree(self):
        # Pressurize Pneumatics
        self.cubemech.startPressurize()

        if (self.gameData == "L"):
            # Turn 90 Degrees Right
            print("Turn")
            self.drivetrain.turnToAngleLeft(80)
        elif (self.gameData == "R"):
            # Stop Driving
            self.drivetrain.stopDrive()
        else:
            # Wait to Continue
            print("Wait")

    @timed_state(duration=1.5, next_state='stateFive')
    def stateFour(self):
        # Pressurize Pneumatics
        self.cubemech.startPressurize()

        if (self.gameData == "L"):
            # Drive to Switch
            print("Go to Switch")
            self.drivetrain.arcadeDrive(0.75, 0)
        elif (self.gameData == "R"):
            # Drive Back to Starting Position(ish)
            print("Go Back to Start")
            self.drivetrain.arcadeDrive(-0.60, -0.20)
        else:
            # Drive Back to Starting Position(ish)
            print("Go Back to Start")
            self.drivetrain.arcadeDrive(-0.60, -0.20)

    @timed_state(duration=2, next_state='stateSix')
    def stateFive(self):
        # Pressurize Pneumatics
        self.cubemech.startPressurize()

        if (self.gameData == "L"):
            # Shoot Cube
            print("Shoot")
            self.cubemech.shootCube()
        elif (self.gameData == "R"):
            # Just Wait
            print("Wait")
        else:
            # Just Wait
            print("Wait") 

    @timed_state(duration=3.25)
    def stateSix(self):
        # Pressurize Pneumatics
        print("Keep Pressurize")
        self.cubemech.startPressurize()
