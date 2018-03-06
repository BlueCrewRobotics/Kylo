
import wpilib

from magicbot import AutonomousStateMachine, tunable, timed_state

from components.DriveTrain import DriveTrain
from components.CubeMech import CubeMech
                    
class Right(AutonomousStateMachine):

    MODE_NAME = 'Right'

    def __init__(self):

        self.drivetrain = DriveTrain
        self.cubemech = CubeMech

        self.driverStation = wpilib.DriverStation.getInstance()

        try:
            self.gameData = self.driverStation.getGameSpecificMessage()[0]
        except IndexError:
            self.gameData = "UNKNOWN"

    @timed_state(duration=2, next_state='stateTwo', first=True)
    def stateOne(self):
        pass

    @timed_state(duration=2, next_state='stateThree')
    def stateTwo(self):
        if (self.gameData == "L"):
            print("MOVE FORWARD")
            self.drivetrain.arcadeDrive(0.5, 0)
        elif (self.gameData == "R"):
            print("SHOOT")


    @timed_state(duration=2, next_state='stateFour')
    def stateThree(self):
        if (self.gameData == "L"):
            print("Turn")
            self.drivetrain.turnToAngle(85.5, 0)
        elif (self.gameData == "R"):
           print("SHOOT")

    @timed_state(duration=2)
    def stateFour(self):
        if (self.gameData == "L"):
            self.drivetrain.arcadeDrive(-0.5, 0)
        elif (self.gameData == "R"):
            pass

        
    
