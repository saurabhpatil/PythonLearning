import random
from combat import Combat

class person(Combat):
	hit_points = 10
	experience = 0
	sound = 'chaaaaarge'
		
	def __init__(self,kwargs):
		self.name = input("Player Name: ")
		self.weapon = self.get_weapon()
		for key, value in **kwargs:
			setattr(self,key,value)
	
	def get_weapon(self):
		weapon_choice = input("Select your weapon([S]word, [A]xe, [B]ow): ")
		if weapon_choice == 's'.casefold():
			return 'Sword'
		elif weapon_choice == 'a'.casefold():
			return 'Axe'
		elif weapon_choice == 'b'.casefold():
			return 'Bow'
		else:
			get_weapon()
	
	def attack(self):
		dyce = random.randint(range(1,10))
		return dyce > 5
		
	def rest(self):
		self.hit_points += 1