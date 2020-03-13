# To the GroundVehicle class, add method drive() that returns "vroooom".
#
# Also change it so the num_wheels defaults to 4 if not specified when the
# object is constructed.

class GroundVehicle():
    def __init__(self, num_wheels=4):
        self.num_wheels = num_wheels
    # method here
    #called drive 
    #looks at num_wheels and returns whatever word if the len is 4
    def drive(self):
        return('vroooom')
    


# Subclass Motorcycle from GroundVehicle.
#
# Make it so when you instantiate a Motorcycle, it automatically sets the number
# of wheels to 2 by passing that to the constructor of its superclass.
#
# Override the drive() method in Motorcycle so that it returns "BRAAAP!!"
# motercycle will get the GV class passed to it due to being a subclass
# def init to be looking for 2 not 4 
# to get info down from GV we need super to get info down into motorcycle
class Motorcycle(GroundVehicle):
    def __init__(self,num_wheels=2):
        super().__init__(num_wheels)
    def drive(self):
        return("BRAAAP!!")

    
vehicles = [
    GroundVehicle(),
    GroundVehicle(),
    Motorcycle(),
    GroundVehicle(),
    Motorcycle(),
]

# Go through the vehicles list and print the result of calling drive() on each.

for d in vehicles:
    print(d.drive())
