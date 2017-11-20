from random import randint 

class Weapon:
	def __init__(self, wtype):
		if wtype == 0:
			self.name = "HersheyKisses"
			self.wtype = wtype
			self.usesLeft = 1000
		if wtype == 1:
			self.name = "SourStraws"
			self.wtype = wtype
			self.usesLeft = 2
		if wtype == 2:
			self.name = "ChocolateBars"
			self.wtype = wtype
			self.usesLeft = 4
		if wtype == 3:
			self.name = "NerdBombs"
			self.wtype = wtype
			self.usesLeft = 1

	def use(self, wtype):
		if wtype == 0:
			return 1
		if wtype == 1:
			self.usesLeft -= 1
			#if no uses left notify player
			return randint(0,75)/100.0 + 1
		if wtype == 2:
			self.usesLeft -= 1
			#if no uses left notify player
			return randint(0,40)/100.0 + 2
		if wtype == 3:
			self.usesLeft -= 1
			#if no uses left notify player
			return randint(50,200)/100.0 + 3

	def get_name(self):
		return self.name

	def get_usesLeft(self):
		return self.usesLeft
