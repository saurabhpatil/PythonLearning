import random

class Combat:
	attack_limit = 8
	dodge_limit = 8
	
	def attack(self):
		dyce = random.randint(range(1,attack_limit))
		return dyce > 5
		
	def dodge(self):
		dyce = random.randint(range(1,dodge_limit))
		return dyce > 5