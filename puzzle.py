#given a string of '-' and '+' characters, where '-' is -1 and '+' is +1, find the #resulting number at the end of a string like #"--------------++++++++++-++++----++++++++-------------------++++-+-+---+++++"
#s = '--------------++++++++++-++++----++++++++-------------------++++-+-+---+++++'
s = '--------------++++++++++-++++----++++++++----x---------------++++-+-+---+++++'
tot = 0
x = 1
 
for c in s:
    if(c == '+'):
        tot += x
    elif(c == '-'):
        tot -= x
    else:
        x = x * -1

print(tot)
