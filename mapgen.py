#!/usr/bin/env python

class Map:
	def __init__(self, ascii, coords):
		self.ascii = ascii
		self.coords = coords

class Room:
	def __init__(self, desc, movPenalty):
		self.desc = desc
		self.movPenalty = movPenalty

class Player:
	def __init__(self, loc):
		self.loc = loc

legend = {
	  '.':'plains'
	, '#':'forest'
	, 'P':'portal'
	, 'C':'castle'
	, '\n':'kljl'
	}

def importMap(str):
	map = {}
	x = 0
	y = 0
	for c in str:
		if c in legend:
			if c == '\n':
				y += 1
				x = 0
				continue
			movPenalty = 0
			desc = ""
			if c == '.':
				desc = 'You are in the plains.'
			elif c == '#':
				desc = 'You are in a forest.'
				movPenalty = 1
			elif c == 'C':
				desc = 'You are in a Castle!.'
			elif c == 'P':
				desc = 'You are at a Portal!.'
			map[(x, y)] = Room(desc, movPenalty)
			x += 1
		else:
			raise AssertionError("invalid character in map")
	return Map(str, map)

def asciiMapWithPlayer(coord, str):
	# coord = (x, y)
	x = coord[0]
	y = coord[1]
	cx, cy = 0, 0
	cx = 0
	cy = 0
	idx = 0
	for c in str:
		if cx == x and cy == y:
			break
		if c == '\n':
			cy += 1
			cx = 0
		else:
			cx += 1
		idx += 1
		#print(c, cx, cy, idx, sep=" ")
	return str[:idx] + '@' + str[idx + 1:]

def navigate(p, m):
	exitCoords = validExits(p.loc, m.coords)
	exitDict = namedExits(p.loc, exitCoords)
	print()
	printExits(exitDict)
	exitChosen = False
	while exitChosen == False:
		print("What do you want to do? (h for help): ")
		com = input()
		if com in exitDict:
			print("You chose", com)
			print()
			exitChosen = True
			p.loc = exitDict[com]
		elif com == 'l':
			print(asciiMapWithPlayer(p.loc, m.ascii))
		elif com == 'h':
			navHelp()
		elif com == 'q':
			exit(0)
		else:
			print("There is nothing there.")

def navHelp():
	helpMsg = '''
	l = look
	n = go north
	s = go south
	e = go east
	w = go west
	q = quit
	'''
	print(helpMsg)

def validExits(coord, coords):
	exits = []
	x = coord[0]
	y = coord[1]
	n = (x, y - 1)
	s = (x, y + 1)
	e = (x + 1, y)
	w = (x - 1, y)
	candidates = [n, s, e, w]
	for c in candidates:
		if c in coords:
			#print(c, "is in dictionary")
			exits.append(c)
	return exits

def namedExits(coord, exitCoords):
	exitDict = {}
	lx = coord[0]
	ly = coord[1]
	for ec in exitCoords:
		x = ec[0]
		y = ec[1]
		if x > lx:
			exitDict['e'] = (x, y)
		elif x < lx:
			exitDict['w'] = (x, y)
		elif y < ly:
			exitDict['n'] = (x, y)
		else:
			exitDict['s'] = (x, y)
	return exitDict

def printExits(exitDict):
	print("Exits: ", end="")
	if 'n' in exitDict:
		print("north ", end="")
	if 's' in exitDict:
		print("south ", end="")
	if 'e' in exitDict:
		print("east " , end="")
	if 'w' in exitDict:
		print("west" , end="")
	print()

# (0, 0)
c1 = '''
#.........
#.........
#....P....
#.....C...
#.........
'''

#print(c1)
#print(len(importMap(c1)))

p = Player((0, 0))
m = importMap(c1.strip())
print(asciiMapWithPlayer(p.loc, m.ascii))

while True:
	# Print room description.
	print(m.coords[p.loc].desc)
	# Take user input to navigate around map.
	navigate(p, m)
	# Show world map with player on it.
	print(asciiMapWithPlayer(p.loc, m.ascii))
	print()