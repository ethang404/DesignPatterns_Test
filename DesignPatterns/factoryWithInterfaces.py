from abc import ABC, abstractmethod
#this example was taken from neetcode.io/problems/factory

#here you have methods of Car/Bike/Truck that simply return it's type
    #this getType method is inherited from Vehicle interface. This isn't necessary relevant to this design pattern

#Vehicle factory is the abstract factory in which will delegate creation to it's children
#CarFactory/BikeFactory/TruckFactory are the concrete implementations of the abstract factory interface

class Vehicle(ABC):
    @abstractmethod
    def getType(self) -> str:
        pass

class Car(Vehicle):
    def getType(self) -> str:
        return "Car"

class Bike(Vehicle):
    def getType(self) -> str:
        return "Bike"

class Truck(Vehicle):
    def getType(self) -> str:
        return "Truck"

class VehicleFactory(ABC):
    @abstractmethod
    def createVehicle(self) -> Vehicle:
        pass

class CarFactory(VehicleFactory):
    # Write your code here
    def createVehicle(self):
        return Car()


class BikeFactory(VehicleFactory):
    # Write your code here
    def createVehicle(self):
        return Bike()

class TruckFactory(VehicleFactory):
    # Write your code here
    def createVehicle(self):
        return Truck()



carFactory = CarFactory()
truckFactory = TruckFactory()
bikeFactory = BikeFactory()

myCar = carFactory.createVehicle()
myTruck = truckFactory.createVehicle()
myBike = bikeFactory.createVehicle()

print(myCar.getType())   # "Car"
print(myTruck.getType()) # "Truck"
print(myBike.getType())  # "Bike"