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

p1 = 20
p2 = 20

def menu():
	msg = '''Choose what you want:
    (c)oin flip"
    (d)ice roll"
    (r)eset both life counters
    (q) -> +1 life to P1
    (w) -> -1 life to P1
    (o) -> +1 life to P2
    (p) -> -1 life to P2
    (x) -> exit
    (h) -> help
	'''
	print(msg)

def printStatus(p1, p2, p1Name, p2Name):
	print(p1Name, p1, p2Name, p2)

if __name__ == "__main__":
	print("Welcome to MagicHelper!")
	print("Enter Player 1's name:")
	p1Name = input()
	print("Enter Player 2's name:")
	p2Name = input()
	menu()
	while True:
		c = getch()
		if c == 'c':
			flip = random.randrange(2) # 0 - 1
			if flip == 0:
				print("Heads")
			else:
				print("Tails")
		elif c == 'd':
			roll = random.randrange(6) # 0 - 5
			print("Dice roll:", roll + 1)
		elif c == 'q':
			p1 += 1
		elif c == 'w':
			p1 -= 1
		elif c == 'o':
			p2 += 1
		elif c == 'p':
			p2 -= 1
		elif c == 'x':
			print("Are you sure you want to exit? (y/n)")
			while True:
				c2 = getch()
				if c2 == 'y':
					exit(0)
				elif c2 == 'n':
					print("OK, continuing...")
					break
				else:
					print("Are you sure you want to exit? (y/n)")
		elif c == 'h':
			menu()
		else:
			printStatus(p1, p2, p1Name, p2Name)

		if c in "cdqwop":
			printStatus(p1, p2, p1Name, p2Name)
