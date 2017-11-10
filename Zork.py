class Player:
	def __init__(self, name):
		self.name = name
		self.HP = 100
		self.attack_rate = 15

p = Player("Rupert")
print(p.name)

p.name = "Nathan"
print(p.name)

print(p.attack_rate)	
