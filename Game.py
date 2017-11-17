from House import House
from Monster import Monster

if __name__ == "__main__":
	house = House(2)
	house.addMonster(Monster(1))
	house.addMonster(Monster(2))
	house.get_monsters()
