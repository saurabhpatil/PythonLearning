import random

class Monster:
    sound = 'roar'
    min_hitpoints = 1
    max_hitpoints = 1
    min_experience = 1
    max_experience = 1
    weapon = 'sword'
    colors = [ "red", "blue", "green", "yellow", "purple", "orange", "white", "black" ]

    def __init__(self,**kwargs):
        self.hit_points = random.randint(self.min_hitpoints,self.max_hitpoints)
        self.experience = random.randint(self.min_experience,self.max_experience))
        self.color = random.choice(colors)
        for key,value in kwargs.items():
            setattr(self,key,value)
    
    def battlecry(self):
        return self.sound.upper()
