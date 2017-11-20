from House import House
from Monster import Monster
from random import randint
from collections import defaultdict
from Weapon import Weapon

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
	
	my_hitpoints = randint(100,125)	
	inventory = []	
	inventory.append(Weapon(0))
	for x in range(9):
		inventory.append(Weapon(randint(1,3)))
	weapon_held = 0
	locationx = 0
	locationy = 0
	
	#possible commands: move NESW, attack, map, inventory, exit, house info
	command = input("Enter a command or help for help: ")
	command.lower()
	while command != "exit":
		if command == "move w":
			if locationy > 0:
				locationy -= 1
			else:
				print("Cannot move west.")
		if command == "move s":
			if locationx < 2:
				locationx += 1
			else:
				print("Cannot move south.")
		if command == "move e":
			if locationy < 2:
				locationy += 1
			else:
				print("Cannot move east.")
		if command == "move n":
			if locationx > 0:
				locationx -= 1
			else:
				print("Cannot move north.")

		if command == "attack":
			monsters = neighborhood[locationx][locationy].getMonsters()
			for x in range(len(monsters)):
				monsters[x].hit(100,0)

		if command == "map":
			for x in range(3):
				for y in range(3):
					if locationx == x and locationy == y:
						print('x', end=" ")
					else:
						print(neighborhood[x][y].get_numMonsters(), end=" ")
				print('\n')
		if command == "status":
			print("Weapons \n")
			for x in range (len(inventory)):
				if x == weapon_held:
					print(x, " ", inventory[x].get_name(), " uses: ", inventory[x].get_usesLeft(), "--IN HAND--")
				else:
					print(x, " ", inventory[x].get_name(), " uses: ", inventory[x].get_usesLeft())
			print("\nMy HP: ", my_hitpoints, '\n')
		if command == "house":
			neighborhood[locationx][locationy].get_monsters()

		if command == "help":
			print("Here is a list of possible commands: move n\e\s\w, attack, map, status, house info, exit")
		
		if command == "weapon":
			input2 = input("Which inventory slot? ").lower()
			wcommand = int(input2)
			if wcommand < 10:
				weapon_held = wcommand
			else:
				print("Enter the inventory slot for the weapon you want, between 0 and 9")
		command = input("Enter a command or help for help: ").lower()
