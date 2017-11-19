from House import House
from Monster import Monster
from random import randint
from collections import defaultdict

if __name__ == "__main__":
	neighborhood = defaultdict(list)
	for x in range(0,3):
		for y in range(0,3):
			num = randint(1,5)
			neighborhood[x,y].append(House(num))
#			for z in range(0,num):
#				m = Monster(randint(0,4))
#				neighborhood[x,y].add_monster(m)
#				m.add_observer(neighborhood[x,y])
	
	for x in range(0,3):
		for y in range(0,3):
			print("House ",x,y)
#			neighborhood[x,y].get_monsters()





	#house = House(2)
	#house.addMonster(Monster(1))
	#house.addMonster(Monster(2))
	#house.get_monsters()
