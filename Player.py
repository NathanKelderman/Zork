from Weapon import Weapon
from random import randint
from observer import Observer

# This is the player class. It stores the hitpoints, location,
# inventory, and which weapon is currently held. It observes the
# weapon class so when a weapon is used up it will be notified and 
# can remove it from the inventory. 
class Player(Observer):

	def __init__ (self):
		self.hitpoints = randint(100,125)
		self.locationx = 0
		self.locationy = 0
		self.inventory = []
		self.inventory.append(Weapon(0))
		for x in range (9):
			self.inventory.append(Weapon(randint(1,3)))
			self.inventory[x+1].add_observer(self)
		self.weapon_held = 0

	def get_hitpoints(self):
		return self.hitpoints

	def get_locationx(self):
		return self.locationx

	def get_locationy(self):
		return self.locationy

	def get_inventory(self):
		return self.inventory

	def get_weapon_held(self):
		return self.weapon_held

	def set_hitpoints(self, num):
		self.hitpoints += num

	def set_locationx(self, move):
		self.locationx += move

	def set_locationy(self, move):
		self.locationy += move

	def set_weapon_held(self, num):
		self.weapon_held = num
	
	def set_inventory(self, update):
		self.inventory = update	

	def update(self, obj):
		self.inventory.remove(obj)
		print("Weapon has run out of uses!")
		self.weapon_held = 0
