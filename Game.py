from House import House
from Monster import Monster
from random import randint
from collections import defaultdict

if __name__ == "__main__":
	neighborhood = []
	for row in range(3):
		neighborhood.append([])
		for col in range(3):
			neighborhood[row].append(House(randint(0,4)))
#	[[House(randint(0,4)) for x in range(3)] for y in range(3)]
#	defaultdict(list)
#	for x in range(0,3):
#		for y in range(0,3):
#			num = randint(1,5)
#			neighborhood[x][y] = House(num)
#			for z in range(0,num):
#				m = Monster(randint(0,4))
#				neighborhood[x,y].add_monster(m)
#				m.add_observer(neighborhood[x,y])	
	for x in range(0,3):
		for y in range(0,3):
			print("House ",x,y)
			neighborhood[x][y].get_monsters()
	
#	monsters = neighborhood[0][0].getMonsters()
	
	locationx = 0
	locationy = 0
	
	#possible commands: move NESW, attack, map, inventory, exit, house info
	command = input("Enter a command or help for help: ")
	command.lower()
	while command != "exit":
		if command == "move n":
			if locationy > 0:
				locationy -= 1
			else:
				print("Cannot move north.")
		if command == "move e":
			if locationx < 2:
				locationx += 1
			else:
				print("Cannot move east.")
		if command == "move s":
			if locationy < 2:
				locationy += 1
			else:
				print("Cannot move south.")
		if command == "move w":
			if locationx > 0:
				locationx -= 1
			else:
				print("Cannot move west.")

		if command == "attack":
			monsters = neighborhood[locationx][locationy].getMonsters()
			for x in range(len(monsters)):
				monsters[x].hit(100,0)

		if command == "map":
			for x in range(0,3):
				print(neighborhood[x][0].get_numMonsters(), neighborhood[x][1].get_numMonsters(), neighborhood[x][2].get_numMonsters())

		if command == "inventory":
			continue#display inventory

		if command == "house":
			neighborhood[locationx][locationy].get_monsters()

		if command == "help":
			print("Here is a list of possible commands: move n\e\s\w, attack, map, inventory, house info, exit") 
		
		command = input("Enter a command or help for help: ").lower()	
