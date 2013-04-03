class Room:
	def__init__(self, desc, mp):
		self.desc = desc
		self.mp = mp
		
class Player:
	def__init__(self, loc):
		self.loc = loc
		
class Map:
	def__init__(self, ascii, coords):
		self.ascii = ascii
		self.coords = coords
	
def importMap(str):
	map = {}
	x = 0
	y = 0
	for (c in c1):
		if c in mapLegend:
			if c == '/n':
				y += 1
				x = 0
				continue
			else:
				x += 1
			movePenalty = 0
			if c == '#':
				movePenalty = 1
			map[(x,y)] = Room('this is a room')
		else:
			raise AssertionError('invalid character in map')
		print(c)
	return map(str,map)
	
mapLegend = {'.':'plains','#':'forest','P':'portal','C':'castle','/n':'aweos'}

def navigate(p,m):
	print(m.ascii)	

c1 = '''
............
#.....P.....
........C...
............
'''

p = Player((0,0))
m = import(c1)

while True:
	navigate(p,m)
	break
chosenPath = input("Choose which path to take, North(N) or South(S)")
if (chosenPath in ['S', 's']):
    print("You have chosen to take the South path!")
elif (chosenPath in ['N', 'n']):
    print("You have chosen to take the North path!")
else:
    chosenPath = input("Choose N or S you moron")

#print(import(map))