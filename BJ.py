#BJ
import random

deck52 = []
suits = 'shcd'
cards = 'A23456789TJQK'

def initDeck():
    for c in cards:
        for s in suits:
            deck52.append(c+s)
    return deck52

myDeck = initDeck()
print(myDeck)

def dealC(myDeck):
    random.shuffle(myDeck)
    tempC = myDeck[0]
    del myDeck[0]
    return (tempC)

def initHands(n):
    myH = []
    dlrH = []
    for c in range(0,n):
        d = [dealC]
        if c == 0 or c % 2:
            myH.extend(d)
        else:
            dlrH.extend(d)
    return [myH, dlrH]
            

#dealer's initial hand

#my initial hand, draw 2 cards
#def initMyHand(myDeck,n):
    #random.shuffle(myDeck)
    #tempC = myDeck[0:n]
    #del myDeck[0:n]
    #return (tempC)
#hand value


t = initHands(4)
print(t)

