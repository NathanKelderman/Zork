from observer import Observer
from observable import Observable
from Monster import Monster
from random import randint


#House class that stores the monsters in the house and notifies
# the neighborhood when the house is cleared
class House(Observer, Observable):

	#Constructor
	def __init__ (self, numMonsters):
		super().__init__()
		self.numMonsters = numMonsters
		self.monstersArray = []
		for x in range(0,numMonsters):
			self.monstersArray.append(Monster(randint(0,4)))
			self.monstersArray[x].add_observer(self)
	#Method for adding classes
	def add_monster(self, monster):
		self.monstersArray.append(monster)
	#Method that returns the monsters in the house
	def get_monsters(self):
		if self.numMonsters == 0:
			print("House is empty!")
		for x in self.monstersArray:
			print (x.get_name(), " HP:", x.get_hitpoints())
	#Getter Method
	def get_numMonsters(self):
		total = 0
		for x in range (self.numMonsters):
			if self.monstersArray[x].get_mtype() != 0:
				total += 1
		return total

	#Update method that notifies the Neighborhood when 
	#the house is cleared
	def update(self, monster):
		num = self.monstersArray.index(monster)
		print(self.monstersArray[num].get_name(), "has been slain!")
		self.monstersArray.remove(monster)
		self.monstersArray.insert(num, Monster(0))
		self.monstersArray[num].add_observer(self)
		if all( x.get_mtype() is 0 for x in self.monstersArray):
			print("House has been cleared!")
			super().update(self)
	#Getter Method
	def getMonsters(self):
		return self.monstersArray

