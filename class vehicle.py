class Vehicle:
    def describe(self):
        print("This is a generic vehicle.")
        
class Car(Vehicle):
    print("This is a sporty car.")

class Motorcycle(Vehicle):
    def describe(self):
        print("This is a fast motorcycle.")

# Make objects from each class
vehicle = Vehicle()
car = Car()
motorcycle = Motorcycle()


