#!/usr/bin/env python

a = 1
print(a, end='f')
print(a)


def fib(n):    # write Fibonacci series up to n
	"""Print a Fibonacci series up to n."""
	a, b = 0, 1
	while a < n:
		print(a, end=' ')
		a, b = b, a+b
	print()

fib(2000)
#fib("fasdf") #error!

# name, attack, hp, defense, initiative
m1 = {'name':'goblin', 'attack':10, 'hp':50, 'defense':5, 'initiative':1}
m2 = {'name':'imp', 'attack':12, 'hp':45, 'defense':4, 'initiative':0}
m3 = {'name':'orc', 'attack':15, 'hp':60, 'defense':5, 'initiative':2}

def fightRound(m1, m2):
	# determine initiative
	# m1 always attacks first
	if (m1['initiative'] > m2['initiative']):
		print(m1['name'], 'attacks first')
		m2['hp'] = m2['hp'] - m1['attack']
		print(m2['name'], 'is now', m2['hp'])
		if (m2['hp'] > 0):
			m1['hp'] = m1['hp'] - m2['attack']
			print(m1['name'], 'is now', m1['hp'])
		else:
			print(m2['name'], 'is dead!')
	else:
		print(m2['name'], 'attacks first')
		m1['hp'] = m1['hp'] - m2['attack']
		print(m1['name'], 'is now', m1['hp'])
		if (m1['hp'] > 0):
			m2['hp'] = m2['hp'] - m1['attack']
			print(m2['name'], 'is now', m2['hp'])
		else:
			print(m1['name'], 'is dead!')
	print(m2['hp'])

def fight(m1, m2):
	while (m1['hp'] > 0 and m2['hp'] > 0):
		fightRound(m1, m2)
	if (m1['hp'] <= 0 and m2['hp'] <= 0):
		print('Both died!')
	elif (m1['hp'] > 0):
		print(m1['name'], 'wins!!!')
	else:
		print(m2['name'], 'wins!!!')

#def isdead(m):
#    return (m1['hp'] > 0)

class Monster:
	def __init__(self, name, attack, hp, ini):
		self.name = name
		self.attack = attack
		self.hp = hp
		self.ini = ini
	def isdead(self):
		return self.hp < 0
	def printStatus(self):
		if (self.isdead()):
			print(self.name, 'is dead!')
		else:
			print(self.name, 'is alive!')

x = Monster('goblin', 10, 50, 1)
print(x)
print(x.name)
print(x.hp)

x.printStatus()

#fight(m1, m3)
#print(m1)
#print(m3)

#if isdead(m3):
    #print(m1['name'], 'is dead!')
