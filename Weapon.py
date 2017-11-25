from random import randint 
from observable import Observable
# This is the weapon class. It stores what type a weapon is and how many
# uses that particular weapon has left. It is being observed by the player
# and notifies the inventory when it runs out of uses.
class Weapon(Observable):
	def __init__(self, wtype):
		super().__init__()
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
	
	# The use method returns the attack modifier as well as remove 1 use from 
	# the weapon and notifies the player if uses are used up
	def use(self):
		if self.wtype == 0:
			return 1
		if self.wtype == 1:
			self.usesLeft -= 1
			if self.usesLeft < 1:
				self.update(self)
			return randint(0,75)/100.0 + 1
		if self.wtype == 2:
			self.usesLeft -= 1
			if self.usesLeft < 1:
				self.update(self)
			return randint(0,40)/100.0 + 2
		if self.wtype == 3:
			self.usesLeft -= 1
			if self.usesLeft < 1:
				self.update(self)
			return randint(50,200)/100.0 + 3

	def get_type(self):
		return self.wtype

	def get_name(self):
		return self.name

	def get_usesLeft(self):
		return self.usesLeft
