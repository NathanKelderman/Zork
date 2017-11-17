from House import House
from Monster import Monster
from random import randint
from collections import defaultdict

if __name__ == "__main__":
	neighborhood = defaultdict(list)
	for x in range(0,3):
		for y in range(0,3):
			neighborhood[x,y] = House(randint(1,5))
	
	
	for x in range(0,3):
		for y in range(0,3):
			print("House ",x,y)
			neighborhood[x,y].get_monsters()





	#house = House(2)
	#house.addMonster(Monster(1))
	#house.addMonster(Monster(2))
	#house.get_monsters()
