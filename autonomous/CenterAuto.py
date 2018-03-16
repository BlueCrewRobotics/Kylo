
import wpilib

from magicbot import AutonomousStateMachine, tunable, timed_state

from components.DriveTrain import DriveTrain
from components.CubeMech import CubeMech
                    
class Center(AutonomousStateMachine):

    MODE_NAME = 'Center'

    def __init__(self):

        self.drivetrain = DriveTrain
        self.cubemech = CubeMech

        self.driverStation = wpilib.DriverStation.getInstance()

        self.gameData = "U"

    @timed_state(duration=2, next_state='stateTwo', first=True)
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
        print("Pressurize")

        if (self.gameData == "L"):
            print("Entering Auto Mode: Center Position Left Switch")
        elif (self.gameData == "R"):
            print("Entering Auto Mode: Center Position Right Switch")
        else:
            print("Entering Auto Mode: Center Position Fail Safe")

    @timed_state(duration=2.0, next_state='stateThree')
    def stateTwo(self):
        # Pressurize Pneumatics
        self.cubemech.startPressurize()

        # Drive Forward
        print("Drive Forward")
        self.drivetrain.arcadeDrive(1.0, 0.4)

    @timed_state(duration=2.6, next_state='stateFour')
    def stateThree(self):
        # Pressurize Pneumatics
        self.cubemech.startPressurize()

        if (self.gameData == "L"):
            # Turn 90 Degrees Left
            print("Turn")
            self.drivetrain.turnToAngleLeft(40)
        elif (self.gameData == "R"):
            # Turn 90 Degrees Right
            print("Turn")
            self.drivetrain.turnToAngleRight(40)
        else:
            print("Wait")

    @timed_state(duration=2.5, next_state='stateFive')
    def stateFour(self):
        # Pressurize Pneumatics
        self.cubemech.startPressurize()
        
        if (self.gameData == "L"):
            # Drive to Switch
            print("Go to Switch")
            self.drivetrain.arcadeDrive(0.75, 0)
        elif (self.gameData == "R"):
            # Drive to Switch
            print("Go to Switch")
            self.drivetrain.arcadeDrive(0.75, 0)
        else:
            # Drive back to Starting Position
            print("Go Back to Start")
            self.drivetrain.arcadeDrive(-1.0, -0.4)

    @timed_state(duration=2, next_state='stateSix')
    def stateFive(self):
        # Pressurize Pneumatics
        self.cubemech.startPressurize()

        if (self.gameData == "L"):
            # Turn 90 Degrees Right
            print("Turn")
            self.drivetrain.turnToAngleRight(40)
        elif (self.gameData == "R"):
            # Turn 90 Degrees Left
            print("Turn")
            self.drivetrain.turnToAngleLeft(40)
        else:
            # Just Wait
            print("Wait")

    @timed_state(duration=2, next_state='stateSeven')
    def stateSix(self):
        # Pressurize Pneumatics
        self.cubemech.startPressurize()

        if (self.gameData == "L"):
            # Drive to Switch
            print("Go to Switch")
            self.drivetrain.arcadeDrive(0.75, 0)
        elif (self.gameData == "R"):
            # Drive to Switch
            print("Go to Switch")
            self.drivetrain.arcadeDrive(0.75, 0)
        else:
            # Just Wait
            print("Wait")

    @timed_state(duration=1)
    def stateSeven(self):
        # Pressurize Pneumatics
        self.cubemech.startPressurize()

        if (self.gameData == "L"):
            # Drop Cube
            print("Shoot")
            self.cubemech.shootCube()
        elif (self.gameData == "R"):
            # Drop Cube
            print("Shoot")
            self.cubemech.shootCube()
        else:
            # Just Wait
            print("Wait")