
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

    @timed_state(duration=2.65, next_state='stateThree')
    def stateTwo(self):
        if (self.gameData == "L"):
            print("MOVE FORWARD")
            self.drivetrain.arcadeDrive(1.0, -0.15)
        elif (self.gameData == "R"):
            # self.drivetrain.arcadeDrive(0, -0.5)
            self.drivetrain.arcadeDrive(1.0, -0.15)
            print("MOVE FORWARD")


    @timed_state(duration=2.5, next_state='stateFour')
    def stateThree(self):
        if (self.gameData == "L"):
            print("DRIVE BACK")
        elif (self.gameData == "R"):
            print("Turn")
            self.drivetrain.arcadeDrive(0, -0.5)
            # self.drivetrain.turnToAngle(85.5, 0)

    @timed_state(duration=2.5, next_state='stateFive')
    def stateFour(self):
        if (self.gameData == "L"):
            pass
        elif (self.gameData == "R"):
            print("DRIVE FORWARD")
            self.drivetrain.arcadeDrive(0.75, 0)

    @timed_state(duration=2)
    def stateFive(self):
        if (self.gameData == "L"):
            pass
        elif (self.gameData == "R"):
            print("SHOOT")
            self.cubemech.shootCube()
        
    
