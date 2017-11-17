from random import randint 

class Weapon:
	def __init__(self, type)
		if type == 0:
			self.name = "HersheyKisses"
			self.type = type
		if type == 1:
			self.name = "SourStraws"
			self.type = type
			self.usesLeft = 2
		if type == 2:
			self.name = "ChocolateBars"
			self.type = type
			self.usesLeft = 4
		if type == 3:
			self.name = "NerdBombs"
			self.type = type
			self.usesLeft = 1

	def use(self, type):
		if type == 0:
			return 1
		if type == 1:
			self.usesLeft -= 1
			#if no uses left notify player
			return randint(0,75)/100.0 + 1
		if type == 2:
			self.usesLeft -= 1
			#if no uses left notify player
			return randint(0,40)/100.0 + 2
		if type == 3:
			self.usesLeft -= 1
			#if no uses left notify player
			return randint(50,200)/100.0 + 3
