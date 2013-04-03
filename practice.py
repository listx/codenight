import random

#cards = [4,4,2]

#a = num aces
#a = 1
#a1 = 10 + a
#sum numbers
#num = sum(cards)

#val = num + a1
#if(a != 0 and val > 21):
    #val -= 10

#print(cards)
#print(num)
#print(val)
#if(val > 21):
#    print(val, 'BUST')

hand = ['Ad', '5s']

a = 4
b = 4

if(str(a) in '89') or (str(b) in '89'):
    print('yes')
else:
    print('no')


def dealHand(shoe):
    playerH = []
    bankerH = []
    #hand values
    p = value(playerH)
    b = value(bankerH)
    #cards hit per side
    numP = 0
    numB = 0
    #natural hand?
    nat = False
    
    for i in range(0,4):
        if i == 0 or i == 2:
            playerH.append(dealC(shoe))
            numP += 1
        else:
            bankerH.append(dealC(shoe))
            numB += 1
    if(str(p) in '89') or (str(b) in '89'):
        nat = True
        print('natural', p, 'to', b)
        print(numP, numB)
    if (nat == False):
        #players third card
        ####PROBLEMS HERE
        if p < 6:
            playerH.append(dealC(shoe))
            numP += 1
        #bankers third card
        if (numP == 3) and (b in range(3,7)):
            if (b == 3 and playerH[2] != 8):
                bankerH.append(dealC(shoe))
            elif (b == 4 and playerH[2] in range(2,8)):
                bankerH.append(dealC(shoe))
            elif (b == 5 and playerH[2] in range(4,8)):
                bankerH.append(dealC(shoe))
            elif (b == 6 and playerH[2] == 6 or 7):
                bankerH.append(dealC(shoe))
        elif b < 6:
            bankerH.append(dealC(shoe))
    return [playerH, bankerH]
