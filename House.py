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
		if self.numMonsters == 0:
			print("House is empty!")
		for x in self.monstersArray:
			print (x.get_name(), " HP:", x.get_hitpoints())
	
	def get_numMonsters(self):
		total = 0
		for x in range (self.numMonsters):
			if self.monstersArray[x].get_mtype() != 0:
				total += 1
		return total

	def update(self):
		print ("Monster updated!")

	def getMonsters(self):
		return self.monstersArray

