#ez bac
import random

#print rules. def RULES

def menu():
    print('''
    
    ''')
#draw board.
#def drawBoard(playerH, dealerH, bet)


#current money total
def availMon(totMon, wages):
    aMon = totMon - wages
    return aMon

#add money
def dep(totMon):
    totMon += 1000
    return totMon

#create shuffled shoe, n is number of decks
def shoe(n):
    decks = []
    for i in range(n):
        for j in 'A23456789TJQK':
            for k in 'shcd':
                decks.append(j+k)
    random.shuffle(decks)
    return decks

#check valid bets, either True for valid or False for invalid:
def placeBet(mon):
    betValid = False
    while(betValid == False):
        print('Place a valid bet, increments of $5')
        b = int(input())
        #what if not a number? error
        if (b % 5 == 0 and 0 <= b <= mon):
            betValid = True
            break
    return b

#ask for player bets.bet is [0 = player, 1 = banker, 2 = tie, 3 = dragon, 4 = panda8]
def wager(totMon):
    spots = ['PLAYER','BANKER','TIE','DRAGON','PANDA']
    bet = [0,0,0,0,0]
    a = 'x'
    while(a not in 'PpBb'):
        print('Do you want to bet on PLAYER(p) or BANKER(b)?')
        a = input()
    if(a in 'Pp'):
        print('How much will you bet on PLAYER?')
        bet[0] = placeBet(totMon)
        print(bet[0], 'on PLAYER')
    else:
        print('How much will you bet on BANKER?')
        bet[1] = placeBet(totMon)
        print(bet[1], 'on BANKER')
    for i in range(2,5):
        print('You may place a', spots[i], 'bet')
        bet[i] = placeBet(totMon)
        print(bet[i], 'on', spots[i])
    wages = sum(bet)
    return [bet, wages]

#draw one card
def dealC(aShoe):
    tempC = aShoe[0]
    del aShoe[0]
    return tempC

#deal the 2 hands
def dealHand(shoe):
    playerH = []
    bankerH = []
    #cards hit per side
    numP = 0
    numB = 0
    #natural hand?
    nat = False
    
    for i in range(4):
        if i == 0 or i == 2:
            playerH.append(dealC(shoe))
            numP += 1
        else:
            bankerH.append(dealC(shoe))
            numB += 1
    p = value(playerH)
    b = value(bankerH)
    if(p in [8, 9]) or (b in [8, 9]):
        nat = True
        #print('natural', p, 'to', b)
        #print(numP, numB)
    if (nat == False):
    #players third card
    ####PROBLEMS HERE
        if p < 6:
            playerH.append(dealC(shoe))
            numP += 1
        #bankers third card
        if (numP == 3) and (b in [3,4,5,6]):
            numB += 1
            if (b == 3 and playerH[2] != 8):
                bankerH.append(dealC(shoe))
            elif (b == 4 and playerH[2] in [2,3,4,5,6,7]):
                bankerH.append(dealC(shoe))
            elif (b == 5 and playerH[2] in [4,5,6,7]):
                bankerH.append(dealC(shoe))
            elif (b == 6 and playerH[2] in [6,7]):
                bankerH.append(dealC(shoe))
            else:
                numB -= 1
        elif b < 6:
            bankerH.append(dealC(shoe))
            numB += 1
    p = value(playerH)
    b = value(bankerH)
    return [playerH, bankerH, numP, numB, p, b]

#add hand values
def value(hand):
    handVal = 0
    for i in hand:
        if i[0] in '23456789':
            j = int(i[0])
            handVal += j
        elif i[0] in 'A':
            handVal += 1
    hV1 = handVal % 10
    return hV1

#determine win/lose, arguments from def dealHand numPlayerCards, numBankerCards, valPlayer, valBanker
def detWinLose(numP, numB, p, b):
    #who wins, 0 = player, 1 = banker, 3 = tie, 4 = dragon, 5 = player/panda
    whoWins = 0
    if


    elif p > b:
        whoWins = 0
    elif b > p:
        whoWins = 1

#start money is 0
#totMon = 0

#totMon = dep(totMon)
#totMon = dep(totMon)
#print(totMon)

#p = wager(totMon)
#print(p)
#a = availMon(totMon, p[1])
#print(a)

newShoe = shoe(8)
results = dealHand(newShoe)
print(results)
