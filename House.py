from Monster import Monster
from random import randint

class House:

	def __init__ (self, numMonsters):
		self.numMonsters = numMonsters
		self.monstersArray = []

	def addMonster (self, Monster):
		self.monstersArray.append(Monster)

	def get_monsters(self):
		for x in self.monstersArray:
			print (x.name)
