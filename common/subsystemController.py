import threading
import time
import wpilib
import wpilib.drive

class subsystemController (threading.Thread):

    def __init__(self, name, controller, joystick, cube, ramp, delay):
        threading.Thread.__init__(self)
        self.name = name
        self.subsystemController = controller
        self.delay = delay
        self.cubemech = cube
        self.ramp = ramp

    def run(self):
        while True:
            
            time.sleep(self.delay)

            # if (self.controller.b()):
            #     print("SEND HELP")
            #     self.cubemech.clampCube()
            if (self.subsystemController.right_bumper()):
                self.cubemech.intakeCube()
            elif (self.subsystemController.left_bumper()):
                self.cubemech.shootCube()
            elif (self.subsystemController.right_trigger()):
                self.cubemech.liftArm()
            elif (self.subsystemController.left_trigger()):
                self.cubemech.lowerArm()
            elif (self.subsystemController.a() and self.subsystemController.x()):
                self.ramp.raiseRightRamp()
            elif (self.subsystemController.a() and self.subsystemController.b()):
                self.ramp.lowerRightRamp()
            else:
                self.cubemech.stop()
                self.ramp.stopRight()
        
    

