from magicbot import AutonomousStateMachine, tunable, timed_state
             
from components.DriveTrain import DriveTrain
                    
class Straight(AutonomousStateMachine):

    MODE_NAME = 'Drive Straight'
    DEFAULT = True
    
    drivetrain = DriveTrain
    
    drive_speed = tunable(0.5)

    @timed_state(duration=4, first=True)
    def moveForward(self):
        print("MOVE FORWARD")
