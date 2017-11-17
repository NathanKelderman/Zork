from random import randint

class Monster:
	def __init__ (self, randNum):
		if randnum == 0:
			self.name = "Person"
			self.hitpoint = 100
			self.mtype = randnum
		if randNum == 1:
			self.name = "Zombie"
			self.hitpoints = randint(50,100)
			self.mtype = randNum
		if randnum == 2:
			self.name = "Vampire"
			self.hitpoints = randint(100, 200)
			self.mtype = randnum
		if randnum == 3:
			self.name = "Ghoul"
			self.hitpoints = randint(40,80)
			self.mtype = randnum
		if randnum == 4:
			self.name = "Werewolf"
			self.hitpoints = 200
			self.mtype = randnum


