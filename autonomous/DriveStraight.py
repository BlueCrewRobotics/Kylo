from magicbot import AutonomousStateMachine, tunable, timed_state
             
from components.DriveTrain import DriveTrain
from components.CubeMech import CubeMech
                    
class Straight(AutonomousStateMachine):

    MODE_NAME = 'Drive Straight'
    DEFAULT = True

    def __init__(self):
    
        self.drivetrain = DriveTrain
        self.cubemech = CubeMech        

    @timed_state(duration=7, next_state='moveForward', first=True)
    def dontMove(self):
        # Pressurize Pneumatics
        self.cubemech.startPressurize()

    @timed_state(duration=3, next_state='stop')
    def moveForward(self):
        # Pressurize Pneumatics
        self.cubemech.startPressurize()

        # Drive Forward
        self.drivetrain.arcadeDrive(0.8, 0.4)
    
    @timed_state(duration=2, next_state='moveBackwards')
    def stop(self):
        # Pressurize Pneumatics
        self.cubemech.startPressurize()

    @timed_state(duration=3)
    def moveBackwards(self):
        # Pressurize Pneumatics
        self.cubemech.startPressurize()

        # Drive Forward
        self.drivetrain.arcadeDrive(-1.0, 0)
