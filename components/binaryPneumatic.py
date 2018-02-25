import wpilib

class BinaryPneuamtic:

    state = False
    
    def __init__(self, solenoidType, name):
    
        self.solenoid = solenoidType
        self.mechName = name

    def switch(self):
      
        if (self.state == False):
            self.solenoid.set(True)
            self.state = True
            wpilib.SmartDashboard.putString(self.mechName, "Engaged")
        elif (self.state == True):
            self.solenoid.set(False)
            self.state = False
            wpilib.SmartDashboard.putString(self.mechName, "Disengaged")
