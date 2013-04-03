#!/usr/bin/env python

import sys

try:
    import tty, termios
except ImportError:
	# Probably Windows.
	try:
		import msvcrt
	except ImportError:
		# FIXME what to do on other platforms?
		# Just give up here.
		raise ImportError('getch not available')
	else:
		getch = msvcrt.getch
else:
	def getch():
		"""getch() -> key character

		Read a single keypress from stdin and return the resulting character.
		Nothing is echoed to the console. This call will block if a keypress
		is not already available, but will not wait for Enter to be pressed.

		If the pressed key was a modifier key, nothing will be detected; if
		it were a special function key, it may return the first character of
		of an escape sequence, leaving additional characters in the buffer.
		"""
		fd = sys.stdin.fileno()
		old_settings = termios.tcgetattr(fd)
		try:
			tty.setraw(fd)
			ch = sys.stdin.read(1)
		finally:
			termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
		return ch

import random


# card -> (suit, deck)
def initDeck52():
	deck = []
	for s in "cdhs":
		for d in "A23456789TJQK":
			deck.append(d + s)
	return deck

def bjValue(cs):
	total = 0
	if hasAce(cs):
		val1 = bjValueNonAces(getNonAces(cs)) + numberOfAces(cs)
		val2 = val1 + 10
		if val2 > 21:
			return (val1, True)
		else:
			return (val2, False)
	else:
		for c in cs:
			total += bjCardValue(c)
		return (total, True)

def bjValueNonAces(cs):
	total = 0
	for c in cs:
		if c[0] == 'A':
			raise AssertError('bjValueNonAces: Ace found')
		total += bjCardValue(c)
	return total

def getNonAces(cs):
	nonAces = []
	for c in cs:
		if c[0] != 'A':
			nonAces.append(c)
	return nonAces

def bjBust(cs):
	return (bjValue(cs)[0] > 21)

def hasAce(cs):
	for c in cs:
		if c[0] == 'A':
			return True
	return False

def numberOfAces(cs):
	n = 0
	for c in cs:
		if c[0] == 'A':
			n += 1
	return n

def isBlackJack(cs):
	# "hello" -> ['h', 'e', 'l', 'l', 'o']
	# x = "hello"
	# x[0] -> 'h'
	# ['Ax', 'Tx']
	# cs[0] -> 'Ax'
	# cs[0][0] -> 'A'
	if len(cs) > 2:
		return False
	elif (cs[0][0] == 'A') and (cs[1][0] in "TJQK"):
		return True
	elif (cs[1][0] == 'A') and (cs[0][0] in "TJQK"):
		return True
	else:
		return False

def bjCardValue(c):
	val = 0
	if c[0] == 'A':
		val = 1
	elif c[0] == '2':
		val = 2
	elif c[0] == '3':
		val = 3
	elif c[0] == '4':
		val = 4
	elif c[0] == '5':
		val = 5
	elif c[0] == '6':
		val = 6
	elif c[0] == '7':
		val = 7
	elif c[0] == '8':
		val = 8
	elif c[0] == '9':
		val = 9
	else:
		val = 10
	return val

if __name__ == "__main__":
	print("Welcome to BJ!")
	mydeck = initDeck52()
	print(mydeck)
	print(len(mydeck))
	print(bjValue(['2c', 'Qh', 'As']))
	print(bjValue(['Ac', 'Qh']))
	print(isBlackJack(['Qc', 'Ah']))
	print(isBlackJack(['Ac', 'Th']))
	print(isBlackJack(['Ac', 'Th', 'Ad']))
