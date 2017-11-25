from House import House
from observer import Observer
from Monster import Monster
from random import randint
from collections import defaultdict
from Weapon import Weapon
from Player import Player
# Neighborhood class to create a neighborhood and populate it with houses
class Neighborhood(Observer):
	def __init__(self):
		self.neighborhood = []
		self.nsize = randint(2,5)
		for row in range(self.nsize):
			self.neighborhood.append([])
			for col in range(self.nsize):
				self.neighborhood[row].append(House(randint(1,10)))
				self.neighborhood[row][col].add_observer(self)
	def get_neighborhood(self):
		return self.neighborhood
	def update(self, house):
		print("House has been cleared!")

# Main method that runs the game. 
if __name__ == "__main__":
	print("WELCOME TO ZORK!")
	# createsinstance of neighborhood
	n = Neighborhood()
	neighborhood = n.get_neighborhood()
	
	# creates instance of a player
	p = Player()
	inventory = p.get_inventory()	
	
	# sets commands in list for easy check
	commands = [ "move n", "move e", "move s", "move w", "attack", "map", "inventory", "exit", "house", "weapon", "help"]
	command = input("Enter a command or 'help' for help and a list of commands: ")
	command.lower()
	
	# loop that exit only if player dies, neighborhood is emptied of monsters or player types 'exit'
	while command != "exit":
		if command not in commands:
			print("Not a valid command. Enter 'help' for a list of commands.")
		if command == "move w":
			if p.get_locationy() > 0:
				p.set_locationy(-1)
			else:
				print("Cannot move west.")
		if command == "move s":
			if p.get_locationx() < (n.nsize-1):
				p.set_locationx(1)
			else:
				print("Cannot move south.")
		if command == "move e":
			if p.get_locationy() < (n.nsize - 1):
				p.set_locationy(1)
			else:
				print("Cannot move east.")
		if command == "move n":
			if p.get_locationx() > 0:
				p.set_locationx(-1)
			else:
				print("Cannot move north.")
		# attack command attacks all monsters in a house with the current weapon in hand
		if command == "attack":
			monsters = neighborhood[p.get_locationx()][p.get_locationy()].getMonsters()
			weap =  inventory[p.get_weapon_held()].get_type()
			atkMod = inventory[p.get_weapon_held()].use()
			for x in range(len(monsters)):
				monsters[x].hit(randint(10,20)* atkMod, weap)
			healthlost = 0
			for x in range(len(monsters)):
				p.set_hitpoints(-monsters[x].attack())
				healthlost += monsters[x].attack()
			print("You lost ", healthlost, " health. \nCurrent HP is ", p.get_hitpoints()) 
			if p.get_hitpoints() < 1:
				print("Oops! You died!")
				break
		# map prints out a double matrix where each spot shows the number of monsters in that house
		# or an 'x' where the plater currently is
		if command == "map":
			for x in range(n.nsize):
				for y in range(n.nsize):
					if p.get_locationx() == x and p.get_locationy() == y:
						print('x', end="   ")
					else:
						print(neighborhood[x][y].get_numMonsters(), end="   ")
				print('\n')
		# status shows the held weapon and players hp
		if command == "status":
			print("Weapon in hand. \n")
			for x in range (len(inventory)):
				if x == p.get_weapon_held():
					print(x, " ", inventory[x].get_name(), " uses: ", inventory[x].get_usesLeft(), "--IN HAND--")
			print("\nMy HP: ", p.get_hitpoints(), '\n')
		# house prints which monsters are currently in the house and how many hitpoints they have left
		if command == "house":
			neighborhood[p.get_locationx()][p.get_locationy()].get_monsters()

		if command == "help":
			print("The goal of Zork is to clear the neighborhood of monsters. A neighbourhood is made up of multiple houses.")
			print("There are 4 possible monsters and there are people. Different weapons effect some monsters differently.")
			print("When 'attacked' the people will give the player back 1 hp. Good luck out there soldier!")
			print("Here is a list of possible commands: move n\e\s\w, attack, map, status, house, weapon, exit")
		
		# weapon is a command to change which weapon is currently in hand
		if command == "weapon":
			for x in range (len(inventory)):
                                if x == p.get_weapon_held():
                                        print(x, " ", inventory[x].get_name(), " uses: ", inventory[x].get_usesLeft(), "--IN HAND--")
                                else:
                                        print(x, " ", inventory[x].get_name(), " uses: ", inventory[x].get_usesLeft())
			input2 = input("Which inventory slot? ").lower()
			wcommand = int(input2)
			if wcommand < 10:
				p.set_weapon_held(wcommand)
			else:
				print("Enter the inventory slot for the weapon you want, between 0 and 9")
		command = input("Enter Input:").lower()
