
#name, attack, hp, defense, initiative
monster1 = {'name':'goblin', 'attack':10,'hp':50,'defense':5,'initiative':1}
monster2 = {'name':'imp', 'attack':12,'hp':45,'defense':4,'initiative':0}
monster3 = {'name':'orc', 'attack':15,'hp':60,'defense':5,'initiative':2}

def fightRound(m1, m2):
    print(m1)
    #determine initiative
    if (m1['initiative'] > m2['initiative']):
        #m1 always attacks first
        print(m1['name'], 'attacks first')
        m2['hp'] = m2['hp'] - m1['attack']
        print(m2['name'], 'is now', m2['hp'])
            if (m2['hp'] > 0):
                m1['hp'] = m1['hp'] - m2['attack']
                print(m1['name'], 'is now', m1['hp'])
            else:
                print(m2['name'], 'died!')

    else:
        print(m2['name'], 'attacks first')
        m1['hp'] = m1['hp'] - m2['attack']
        print(m1['name'], 'is now', m1['hp'])
            if (m1['hp'] > 0):
                m2['hp'] = m2['hp'] - m1['attack']
                print(m2['name'], 'is now', m2['hp'])
            else:
                print(m1['name'], 'died!')

def fight(m1, m2):
    while (m1['hp'] > 0 and m2['hp'] > 0):
        fightRound()


