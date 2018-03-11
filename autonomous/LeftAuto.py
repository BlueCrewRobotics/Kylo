
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

        # Try to Collect Switch Position Data
        try:
            self.gameData = self.driverStation.getGameSpecificMessage()[0]
        except IndexError:
            self.gameData = "UNKNOWN"

        # Print Switch Position (In event of failure for debugging)
        self.driverStation.reportError("Auto Switch Position: " + self.gameData, False)
        print("Auto Switch Position: " + self.gameData)

    @timed_state(duration=2, next_state='stateTwo', first=True)
    def stateOne(self):
        # Pressurize Pneumatics
        self.cubemech.startPressurize()

    @timed_state(duration=2.0, next_state='stateThree')
    def stateTwo(self):
        # Pressurize Pneumatics
        self.cubemech.startPressurize()

        # Drive Forward
        if (self.gameData == "L"):
            self.drivetrain.arcadeDrive(1.0, 0.4)
        elif (self.gameData == "R"):
            self.drivetrain.arcadeDrive(1.0, 0.4)

    @timed_state(duration=2.6, next_state='stateFour')
    def stateThree(self):
        # Pressurize Pneumatics
        self.cubemech.startPressurize()

        if (self.gameData == "L"):
            # Turn 90 Degrees Right
            #self.drivetrain.arcadeDrive(0, 0.5)
            self.drivetrain.turnToAngleLeft(85)
        elif (self.gameData == "R"):
            # Wait to Continue
            pass

    @timed_state(duration=2.5, next_state='stateFive')
    def stateFour(self):
        # Pressurize Pneumatics
        self.cubemech.startPressurize()

        if (self.gameData == "L"):
            # Drive to Switch
            self.drivetrain.arcadeDrive(0.75, 0)
        elif (self.gameData == "R"):
            # Drive Back to Starting Position(ish)
            self.drivetrain.arcadeDrive(-1.0, -0.4)

    @timed_state(duration=2, next_state='stateSix')
    def stateFive(self):
        # Pressurize Pneumatics
        self.cubemech.startPressurize()

        if (self.gameData == "L"):
            # Shoot Cube
            self.cubemech.shootCube()
        elif (self.gameData == "R"):
            # Just Pass
            pass

    @timed_state(duration=3.25)
    def stateSix(self):
        # Pressurize Pneumatics
        self.cubemech.startPressurize()
