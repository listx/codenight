#!/usr/bin/env python

import random

lootType = ["Helm", "Boots", "Gloves", "Pants", "Pike", "Axe", "Sword", "Bracers", "Shoulders", "Amulet", "Ring"]
resistType = ["Physical", "Cold", "Poison", "Arcane", "Fire", "Lightning", "Holy", "Infernal", "Vampiric", "Natural", "Occult", "Explosive"]
legendaryType = ["of the Snake", 'from the Leong Clan', 'of the Hokage', 'from the Water Closet']

def genResist():
	perc = random.randrange(1, 101)
	resist = random.choice(resistType)
	return '\n\t' + str(perc) + '% ' + resist + ' resist'

def makeLoot():
	loot = random.choice(lootType)
	legendaryFactor = random.randrange(10)
	if legendaryFactor > 7:
		lootDesc = random.choice(legendaryType)
		loot += ' ' + lootDesc
	for i in range(random.randrange(4)):
		loot += genResist()
	if legendaryFactor > 7:
		for i in range(random.randrange(6, 10)):
			loot += genResist()
	return loot

print(makeLoot())
