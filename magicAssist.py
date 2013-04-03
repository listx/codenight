import random

MENU = '''
Choose function below:
(m)enu
(c)oin flip
(d)6 roll
(q) +1 to player 1 life total
(Q) +5 to player 1 life total
(w) -1 to player 1 life total
(W) -5 to player 1 life total
(o) +1 to player 2 life total
(O) +5 to player 2 life total
(p) -1 to player 2 life total
(P) -5 to player 2 life total
(r)eset both player's life totals
'''

def score(p1hp, p2hp):
    print(p1n,':',p1hp,'\t', p2n,':',p2hp)
    #how to do draw?
    if(p1hp <= 0):
        print(p1n, 'has lost the game!')
    elif(p2hp <= 0):
        print(p2n, 'has lost the game!')

print('Enter the name of player 1:')
p1n = input(str)
print('Enter the name of player 2:')
p2n = input(str)

p1hp = 20
p2hp = 20

print(MENU)

while True:
    c = input()
    if(c == 'm'):
        print(MENU)
    elif(c == 'c'):
        if(random.randint(0,1) == 0):
            print('heads')
        else:
            print('tails')
    elif(c == 'd'):
        print(random.randint(1,6))
    elif(c == 'q'):
        p1hp += 1
    elif(c == 'Q'):
        p1hp += 5
    elif(c == 'w'):
        p1hp -= 1
    elif(c == 'W'):
        p1hp -= 5
    elif(c == 'o'):
        p2hp += 1
    elif(c == 'O'):
        p2hp += 5
    elif(c == 'p'):
        p2hp -= 1
    elif(c == 'P'):
        p2hp -= 5
    elif(c == 'r'):
        p1hp = 20
        p2hp = 20
        print(p1n, 'and', p2n, 'has life reset to', p1hp)
    if(c in 'qQwWoOpPr'):
        score(p1hp,p2hp)


