
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

    @timed_state(duration=2, next_state='stopDrive', first=True)
    def stateOne(self):
        if (self.gameData == "L"):
            self.drivetrain.arcadeDrive(0.35)
        elif (self.gameData == "R"):
            print("MOVE FORWARD")

    @timed_state(duration=1)
    def stopDrive(self):
        self.drivetrain.arcadeDrive(0)

    @timed_state(duration=2, next_state='stateThree')
    def stateTwo(self):
        if (self.gameData == "L"):
            print("TURN NINETY")
        elif (self.gameData == "R"):
            print("TURN NINETY")

    @timed_state(duration=2, next_state='stateFour')
    def stateThree(self):
        if (self.gameData == "L"):
            print("MOVE FORWARD")
        elif (self.gameData == "R"):
            print("MOVE FORWARD")

    @timed_state(duration=2)
    def stateFour(self):
        if (self.gameData == "L"):
            print("SHOOT")
        elif (self.gameData == "R"):
            print("SHOOT")
