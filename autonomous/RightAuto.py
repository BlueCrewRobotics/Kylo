
import wpilib

from magicbot import AutonomousStateMachine, tunable, timed_state

from components.DriveTrain import DriveTrain
                    
class Right(AutonomousStateMachine):

    MODE_NAME = 'Right'

    def __init__(self):

        self.drivetrain = DriveTrain

        self.driverStation = wpilib.DriverStation.getInstance()

        try:
            self.gameData = self.driverStation.getGameSpecificMessage()[0]
        except IndexError:
            self.gameData = "UNKNOWN"

    @timed_state(duration=2, next_state='stateTwo', first=True)
    def stateOne(self):
        if (self.gameData == "L"):
            print("MOVE FORWARD")
        elif (self.gameData == "R"):
            print("MOVE FORWARD")

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
            print("SHOOT")

    @timed_state(duration=2, next_state='stateFive')
    def stateFour(self):
        if (self.gameData == "L"):
            print("TURN NINETY")
        elif (self.gameData == "R"):
            pass

    @timed_state(duration=2)
    def stateFive(self):
        if (self.gameData == "L"):
            print("SHOOT")
        elif (self.gameData == "R"):
            pass
