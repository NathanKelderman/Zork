from observer import Observer
from Monster import Monster
from random import randint

class House(Observer):

	def __init__ (self, numMonsters):
		self.numMonsters = numMonsters
		self.monstersArray = []
		for x in range(0,numMonsters):
			self.monstersArray.append(Monster(randint(0,4)))
			self.monstersArray[x].add_observer(self)
	
	def add_monster(self, monster):
		self.monstersArray.append(monster)

	def get_monsters(self):
		for x in self.monstersArray:
			print (x.get_name())
	
	def get_numMonsters(self):
		return self.numMonsters

	def update(self):
		print ("Monster updated!")

	def getMonsters(self):
		return self.monstersArray

