from random import randint

class Monster:
	def __init__ (self, randNum):
		if randNum == 1:
			self.name = "Zombie"
			self.hitpoints = randint(50,100)
			self.mtype = randNum


