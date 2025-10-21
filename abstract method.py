from abc import ABC, abstractmethod

#Abstractn Base Class
class Vehical(ABC):
    @absrtactmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    def refuel(self):
        print("Refueling the vehicle.")

#Concrete Subclass: Car
class Car(Vehicle):
    def start(self):
        print("Car engine started.")

    def stop(self):
        print("Car engine stopped.")

#Concrete Subclass: Motorcycle
class Motorcycle(Vehicle):
