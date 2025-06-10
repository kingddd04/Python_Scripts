""" 
An object-oriented programming example that simulates a fight between a hero and a zombie.
This code defines two classes, Hero and Zombie, each with methods to attack and decrease health.
An objet is an absstrac representation of a real-world entity, with properties in form of attributes 
An object has methods that define how it behaves or interacts with other objects.
"""
class Hero:
    """A class representing a charcter in a fighting game."""
    def __init__(self, name, health, strenght): # this is the constructor method
        """Initializes the Hero with a name, health, and strength."""
        self.name = name 
        self.health = health 
        self.strenght = strenght
        
    def attack_enemy(self, enemy) :   
        """Attacks an enemy and decreases its health by the hero's strength."""
        enemy.decrease_hp(self.strenght)
        
    def decrease_hp(self, strenght):
        """Decreases the hero's health by the enemy given strength."""
        self.health -= strenght
        
        
    
class Zombie:
    """A class representing a strong zombie character in a fighting game."""
    def __init__(self, name , health, strenght): # this is the constructor method
        self.name = name 
        self.health = health
        self.strenght = strenght
        
    def attack_enemy(self, enemy):
        """Attacks an enemy and decreases its health by the zombie's strength."""
        enemy.decrease_hp(self.strenght)
        
        
    def decrease_hp(self, strenght):
        """Decreases the zombie's health by the given strength of the enemy."""
        self.health -= strenght
        
    
def fight():
    """Main function to simulate a fight between the hero and a zombie."""
    
    hero = Hero("Spartaco", 100, 20) # Creates a hero object with name, health, and strength
    zombie = Zombie("Zombie Boss", 80, 15) # Creates a zombie object with name, health, and strength
    
    while hero.health > 0 and zombie.health > 0:  
        hero.attack_enemy(zombie)
        print(f"{hero.name} attacks {zombie.name}. {zombie.name} health: {zombie.health}\n")
        zombie.attack_enemy(hero)
        print(f"{zombie.name} attacks {hero.name}. {hero.name} health: {hero.health}\n")
        if hero.health <= 0:
            print(f"{hero.name} has been defeated by {zombie.name}.\n")
            break
        elif zombie.health <= 0:
            print(f"{zombie.name} has been defeated by {hero.name}.\n")
            break
        
fight()  # Call the fight function to start the simulation