from magicbot import AutonomousStateMachine, tunable, timed_state
             
from components.DriveTrain import DriveTrain
from components.CubeMech import CubeMech
                    
class Straight(AutonomousStateMachine):

    MODE_NAME = 'Drive Straight'
    DEFAULT = True
    
    self.drivetrain = DriveTrain
    self.cubemech = CubeMech
    
    drive_speed = tunable(0.5)

    @timed_state(duration=7, next_state='moveForward', first=True)
    def dontMove(self):
        # Pressurize Pneumatics
        self.cubemech.startPressurize()

    @timed_state(duration=3, next_state='pressurize')
    def moveForward(self):
        # Pressurize Pneumatics
        self.cubemech.startPressurize()

        # Drive Forward
        self.drivetrain.arcadeDrive(1.0, 0)

    @timed_state(duration=5)
    def pressurize(self):
        # Pressurize Pneumatics
        self.cubemech.startPressurize()
