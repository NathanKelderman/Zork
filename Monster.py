from random import randint

class Monster:
	def __init__ (self, randNum):
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

	def get_name(self):
		return self.name
	def get_hitpoints(self):
		return self.hitpoints
	def get_mtype(self):
		return self.mtype
