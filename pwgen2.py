#!/usr/bin/env python

import random as rand
import getopt, sys

letters = 'abcdefghijklmnopqrstuvwxyz'
lettersCaps = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '1234567890'
puncs = '`~!@#$%^&*()-_=+[{]}\\|;:\'",<.>/?'
allChars = letters + lettersCaps + numbers + puncs

def pwgen(n):
	str = ''
	for i in range(n):
		str += rand.choice(allChars)
	return str

def usage():
	print("pwgen2.py -n LENGTH")

def main():
	try:
		opts, args = getopt.getopt(sys.argv[1:], "hn:v", ["help", "length="])
	except getopt.GetoptError as err:
		# print help information and exit:
		print(err) # will print something like "option -a not recognized"
		usage()
		sys.exit(2)
	passLength = 8
	verbose = False
	for o, a in opts:
		if o == "-v":
			verbose = True
		elif o in ("-h", "--help"):
			usage()
			sys.exit()
		elif o in ("-n", "--length"):
			try:
				passLength = int(a)
			except ValueError as err:
				print(err)
				sys.exit(2)
		else:
			assert False, "unhandled option"

	#print(letters, lettersCaps, numbers, puncs)
	#print(len(letters + lettersCaps + numbers + puncs))

	print(pwgen(passLength))

if __name__ == "__main__":
    main()
