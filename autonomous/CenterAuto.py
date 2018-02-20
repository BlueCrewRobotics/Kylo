
import wpilib

from magicbot import AutonomousStateMachine, tunable, timed_state

from components.DriveTrain import DriveTrain
                    
class Center(AutonomousStateMachine):

    MODE_NAME = 'Center'

    def __init__(self):

        self.drivetrain = DriveTrain

        self.driverStation = wpilib.DriverStation.getInstance()

        try:
            self.gameData = self.driverStation.getGameSpecificMessage()[0]
        except IndexError:
            self.gameData = "UNKNOWN"

    @timed_state(duration=2, next_state='moveSecond', first=True)
    def moveForward(self):
        if (self.gameData == "L"):
            print("LEFT")
        elif (self.gameData == "R"):
            print("RIGHT")

    @timed_state(duration=2)
    def moveSecond(self):
        print("CENTER SECOND")
