from magicbot import AutonomousStateMachine, tunable, timed_state
             
from components.DriveTrain import DriveTrain
from components.CubeMech import CubeMech
                    
class Test(AutonomousStateMachine):

    MODE_NAME = 'Test'

    def __init__(self):
    
        self.drivetrain = DriveTrain
        self.cubemech = CubeMech        

    @timed_state(duration=5, next_state='turnRight', first=True)
    def turnLeft(self):
        self.drivetrain.turnToAngleLeft(85)

    @timed_state(duration=5)
    def turnRight(self):
        self.drivetrain.turnToAngleRight(85)