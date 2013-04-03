#!/usr/bin/env python

choseValidDirection = False

while (choseValidDirection == False):
	chosenPath = input("Choose which path to take, North(N) or South(S)")
	if (chosenPath in ['S', 's']):
		print("You have chosen to take the South path!")
		choseValidDirection = True
	elif (chosenPath in ['N', 'n']):
		print("You have chosen to take the North path!")
		choseValidDirection = True
	else:
		chosenPath = input("Choose N or S you moron")
