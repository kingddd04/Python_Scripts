""" 
In this script we shall work with class inheritance in Python.
We create a class animal, then a class Mammal an then single annimal classes like Cat and Platipus.
We will pass the prroprieties of the parent class to the child classes.
"""

class Animal:
    def __init__(self, name): # the name is given by the user
        self.name = name

    def speak(self):
        print("Animal speaks")  # This is a generic method that can be overridden by child classes

    

class Mammal(Animal): # The class takes as argument its parent class Animal
    def __init__(self, name):
        super().__init__(name) # call the constructor of the parent class with the name given by the user
        self.is_endothermic = True
        self.is_viviparous = True
        self.breast_feed = True
        
    def breastfeed(self):
        print(self.name + " is breastfeeding its young.")

class Cat(Mammal):  # The class takes as argument its parent class Mammal wich is a child of Animal
    def __init__(self, name):
        super().__init__(name)
        self.hasFur = True
    def speak(self):
        return "Meow"
    
    
class Platipus(Mammal): # The class takes as argument its parent class Mammal wich is a child of Animal
    def __init__(self, name):
        super().__init__(name)
        self.is_ovivipary = True
        
    def layeggs(self):
        print(self.name + " is laying eggs.")
    
    def speak(self):
        return "Prrr"
    
    
def ciao():
    cat = Cat("Cat")
    print(cat.name + " says: " + cat.speak())
    cat.breastfeed()
    
    platipus = Platipus("Perry")
    print(platipus.name + " says: " + platipus.speak())
    platipus.layeggs()
    platipus.breastfeed()
    
    
    
if __name__ == "__main__":
    ciao()