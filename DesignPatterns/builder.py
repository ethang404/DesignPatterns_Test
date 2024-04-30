

#The builder pattern is another creational pattern
#It is useful to abstract data out of the constructor, while also
    #providing specific options to "build" your object. Instead of having constructor overrides for each setup


#Here we can have a "creature". And you can set specific attributes for a creature using builder pattern(CreaterBuilder)

class Creature:
    def __init__(self):
        self.numLegs = None
        self.numEyes = None
        self.sex = None
    #define setters for each attribute
    def setNumLegs(self, legNumber):
        self.numLegs = legNumber
    def setnumEyes(self, eyeNumber):
        self.numEyes = eyeNumber
    def setSex(self, sex):
        self.sex = sex

class CreatureBuilder:
    def __init__(self):
        #have a instance of Creature Object to manipulate
        self.creature = Creature()

    def addLegs(self, legs):
        self.creature.setnumLegs(legs)
        return self

    def addEyes(self, legs):
        self.creature.setnumEyes(legs)
        return self

    #etc..
    def build(self):
        return self.creature
    
#use builder to create creature
#returns creature instance
creature = CreatureBuilder().addLegs(4).addEyes(2).build()

#Note: the builder class isn't technically necessary either,
#you can just have the sets in the Creature  and call the method and return self.
