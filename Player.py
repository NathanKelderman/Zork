from Weapon import Weapon

class Player

	def __init__ (self)
		self.hitpoints = randint(100,125)
		self.locationx = 0
		self.locationy = 0
		self.inventory = []
		self.inventory.append(Weapon(0))
		for x in range (9)
			inventory.append(Weapon(randint(1,3)))
		self.weapon_held = 0

	def get_hitpoints(self)
		return self.hitpoints

	def get_locationx(self)
		return self.locationx

	def get_locationy(self)
		return self.locationy

	def get_inventory(self)
		return self.inventory

	def get_weapon_held(self)
		return self.weapon_held	
