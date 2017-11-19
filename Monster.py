from observable import Observable
from random import randint

class Monster(Observable):
	def __init__ (self, randNum):
		super().__init__()
		if randNum == 0:
			self.name = "Person"
			self.hitpoint = 100
			self.mtype = randNum
		if randNum == 1:
			self.name = "Zombie"
			self.hitpoints = randint(50,100)
			self.mtype = randNum
		if randNum == 2:
			self.name = "Vampire"
			self.hitpoints = randint(100, 200)
			self.mtype = randNum
		if randNum == 3:
			self.name = "Ghoul"
			self.hitpoints = randint(40,80)
			self.mtype = randNum
		if randNum == 4:
			self.name = "Werewolf"
			self.hitpoints = 200
			self.mtype = randNum
		self.update()

	def get_name(self):
		return self.name
	def get_hitpoints(self):
		return self.hitpoints
	def get_mtype(self):
		return self.mtype

	def attack(self):
		if self.mtype == 0:
			return -1
		if self.mtype == 1:
			return randint(0,10)
		if self.mtype == 2:
			return randint(10,20)
		if self.mtype == 3:
			return randint(15,30)
		if self.mtype == 4:
			return randint(0,40)

	def hit(self, atk, weapon):
		if self.mtype == 1:
			if weapon == 1:
				self.hitpoints -= atk*2
			else: 
				self.hitpoints -= atk
			if self.hitpoints < 1:
				#self.update()
				self.name = "Person"
				self.hitpoint = 100
				self.mtype = randNum
		if self.mtype == 2:
			if weapon == 2: 
				pass
			else: 
				self.hitpoints -= atk
			if self.hitpoints < 1:
				#notify house
				self.name = "Person"
				self.hitpoint = 100
				self.mtype = randNum
		if self.mtype == 3:
			if weapon == 3:
				self.hitpoints -= atk*5
			else: 
				self.hitpoints -= atk
			if self.hitpoints < 1:
				#notify house
				self.name = "Person"
				self.hitpoint = 100
				self.mtype = randNum
		if self.mtype == 4:
			if weapon == 1 or weapon == 2: 
				pass
			else: 
				self.hitpoints -= atk
			if self.hitpoints < 1:
				#notify house
				self.name = "Person"
				self.hitpoint = 100
				self.mtype = randNum
