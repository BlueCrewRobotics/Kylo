import wpilib

class binaryPneuamtics:

    state = False

    solenoid  = None

    mechName = None
    
    def __init__(self, solenoidType, name):

        self.solenoid = solenoidType

        self.mechName = name

    def switch(self):

        if (self.state == False):
            self.intakeSolenoid.set(True)
            self.state = True
            wpilib.SmartDashboard.putString(mechName, "Engaged")
        elif (self.state == True):
            self.intakeSolenoid.set(False)
            self.state = False
            wpilib.SmartDashboard.putString(mechName, "Disengaged")
