from House import House
from observer import Observer
from Monster import Monster
from random import randint
from collections import defaultdict
from Weapon import Weapon
from Player import Player

class Neighborhood(Observer):
	def __init__(self):
		self.neighborhood = []
		for row in range(3):
			self.neighborhood.append([])
			for col in range(3):
				self.neighborhood[row].append(House(randint(0,4)))
				self.neighborhood[row][col].add_observer(self)
	def get_neighborhood(self):
		return self.neighborhood


if __name__ == "__main__":
	n = Neighborhood()
	neighborhood = n.get_neighborhood()
	
	p = Player()
	inventory = p.get_inventory()	
	
	commands = [ "move n", "move e", "move s", "move w", "attack", "map", "inventory", "exit", "house", "weapon"]
	command = input("Enter a command or help for help: ")
	command.lower()
	while command != "exit":
		if command not in commands:
			print("Not a valid command.")
		if command == "move w":
			if p.get_locationy() > 0:
				p.set_locationy(-1)
			else:
				print("Cannot move west.")
		if command == "move s":
			if p.get_locationx() < 2:
				p.set_locationx(1)
			else:
				print("Cannot move south.")
		if command == "move e":
			if p.get_locationy() < 2:
				p.set_locationy(1)
			else:
				print("Cannot move east.")
		if command == "move n":
			if p.get_locationx() > 0:
				p.set_locationx(-1)
			else:
				print("Cannot move north.")

		if command == "attack":
			monsters = neighborhood[p.get_locationx()][p.get_locationy()].getMonsters()
			for x in range(len(monsters)):
				monsters[x].hit(100,0)

		if command == "map":
			for x in range(3):
				for y in range(3):
					if p.get_locationx() == x and p.get_locationy() == y:
						print('x', end=" ")
					else:
						print(neighborhood[x][y].get_numMonsters(), end=" ")
				print('\n')
		if command == "status":
			print("Weapons \n")
			for x in range (len(inventory)):
				if x == p.get_weapon_held():
					print(x, " ", inventory[x].get_name(), " uses: ", inventory[x].get_usesLeft(), "--IN HAND--")
				else:
					print(x, " ", inventory[x].get_name(), " uses: ", inventory[x].get_usesLeft())
			print("\nMy HP: ", p.get_hitpoints(), '\n')
		if command == "house":
			neighborhood[p.get_locationx()][p.get_locationy()].get_monsters()

		if command == "help":
			print("Here is a list of possible commands: move n\e\s\w, attack, map, status, house, weapon, exit")
		
		if command == "weapon":
			input2 = input("Which inventory slot? ").lower()
			wcommand = int(input2)
			if wcommand < 10:
				p.set_weapon_held(wcommand)
			else:
				print("Enter the inventory slot for the weapon you want, between 0 and 9")
		command = input("Enter a command or help for help: ").lower()
