from magicbot import AutonomousStateMachine, tunable, timed_state
             
from components.DriveTrain import DriveTrain
                    
class Straight(AutonomousStateMachine):

    MODE_NAME = 'Drive Straight'
    DEFAULT = True
    
    drivetrain = DriveTrain
    
    drive_speed = tunable(0.5)

    @timed_state(duration=7, next_state='moveForward', first=True)
    def dontMove(self):
        self.drivetrain.arcadeDrive(1.0, 0)

    @timed_state(duration=3.5)
    def moveForward(self):
        self.drivetrain.arcadeDrive(1.0, 0)
