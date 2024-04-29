

#this is a factory(method) design pattern. 

#All the logic is, is a way to abstract the creation of an object to another class.
#This is good for 2 reasons:
#1) To only have one place to create objects(DRY)
#2) We're able to easily expand logic to creating another object by adding
    #another class and adding a new factory.


class WeinerDog:
    def __init__(self, size):
        self.size = size
        self.name = "Weiner"

    def print(self):
        print(str(self.size) + " and " + self.name)

class MastiffDog:
    def __init__(self, size):
        self.size = size
        self.name = "Mastiff"

    def print(self):
        print(str(self.size) + " and " + self.name)

class DogFactory:
    def createWeinerDog(self):
        size = 1
        return WeinerDog(size)
    
    def createMastiff(self):
        size = 10
        return MastiffDog(size)
    

#Create a dog factory object
dogFactory = DogFactory()

#create dog objects using the factory
dogFactory.createWeinerDog().print()
dogFactory.createMastiff().print()

#We can also add a cat to our "DogFactory" if we wanted to expand our logic...although it does make more sense to make 
    #a cat factory.