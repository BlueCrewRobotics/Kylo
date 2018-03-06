from magicbot import AutonomousStateMachine, tunable, timed_state
             
from components.DriveTrain import DriveTrain
                    
class Straight(AutonomousStateMachine):

    MODE_NAME = 'Drive Straight'
    DEFAULT = True
    
    drivetrain = DriveTrain
    
    drive_speed = tunable(0.5)

    @timed_state(duration=1, next_state='moveForward', first=True)
    def dontMove(self):
        self.drivetrain.arcadeDrive(0.5, 0)

    @timed_state(duration=3)
    def moveForward(self):
        self.drivetrain.arcadeDrive(0.5, 0)
