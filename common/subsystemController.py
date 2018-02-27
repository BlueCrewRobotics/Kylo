'''

 -- Subsystems Controller --

Blue Crew Robotics Team 6153
Authors: Jacob Mealey, Matthew Gallant

'''

import threading
import time
import wpilib
import wpilib.drive
from common.subsystemButtons.intakeControls import intakeControls

class subsystemController (threading.Thread):

    def __init__(self, name, controller, joystick, cube, ramp, delay):
        threading.Thread.__init__(self)
        self.name = name
        self.subsystemController = controller
        self.delay = delay
        self.cubemech = cube
        self.ramp = ramp
        self.intake = intakeControls(cube, controller, joystick, delay)

    def run(self):
        while True:
            
            time.sleep(self.delay)
            self.intake.run()
            # if (self.subsystemController.right_bumper()):
            #     self.cubemech.intakeCube()
            # elif (self.subsystemController.left_bumper()):
            #     self.cubemech.shootCube()
            if (self.subsystemController.right_trigger()):
                self.cubemech.liftArm()
            elif (self.subsystemController.left_trigger()):
                self.cubemech.lowerArm()
            elif (self.subsystemController.a() and self.subsystemController.y()):
                self.ramp.deployRamps()
            elif (self.subsystemController.a() and self.subsystemController.x()):
                self.ramp.raiseRightRamp()
            elif (self.subsystemController.a() and self.subsystemController.b()):
                self.ramp.lowerRightRamp()
            elif (self.subsystemController.b()):
                self.cubemech.clampCube()
            elif (self.subsystemController.x()):
                self.cubemech.startPressurize()
            else:
                self.cubemech.stop()
                self.ramp.stopRight()
                self.cubemech.stopPressurize()
        
    

