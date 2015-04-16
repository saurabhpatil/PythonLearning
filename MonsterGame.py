import random

class Monster:
    sound = 'roar'
    min_hitpoints = 1
    max_hitpoints = 1
    min_experience = 1
    max_experience = 1
    weapon = ['sword','axe','bow','club','spear']
    colors = [ "red", "blue", "green", "yellow", "purple", "orange", "white", "black" ]

    def __init__(self,**kwargs):
        self.hit_points = random.randint(self.min_hitpoints,self.max_hitpoints)
        self.experience = random.randint(self.min_experience,self.max_experience))
        self.color = random.choice(colors)
        self.weapon = random.choise(weapon)
        for key,value in kwargs.items():
            setattr(self,key,value)
    
    def battlecry(self):
        return self.sound.upper()

class Troll(Monster):
    sound = 'Grrrrrrrrr'
    min_hitpoints = 1
    max_hitpoints = 5
    min_experience = 1
    max_experience = 3

class Cyclops(Monster):
    sound = 'Yahhhhhhh'
    min_hitpoints = 2
    max_hitpoints = 6
    min_experience = 2
    max_experience = 5

class Minotaur(Monster):
    sound = 'Hussssssss'
    min_hitpoints = 4
    max_hitpoints = 8
    min_experience = 5
    max_experience = 8

class Dragon(Monster):
    sound = 'Raaaaaaaaa'
    min_hitpoints = 6
    max_hitpoints = 10
    min_experience = 8
    max_experience = 10
        
    
