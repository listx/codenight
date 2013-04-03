class Mon:
	def __init__(self, name, atk, hp, ini):
		self.name = name
		self.attack = atk
		self.hp = hp
		self.ini = ini
	def isdead(self):
		return self.hp < 0
	def printStatus(self):
		if (self.isdead()):
			print(self.name, 'is dead')
		else:
			print(self.name, 'is alive')

x = Mon('goblin', 10, 50, 1)

x.printStatus()