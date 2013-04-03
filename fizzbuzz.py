for numberrr in range(1,101):
    if (numberrr % 15 == 0):
        print('fizzbuzz')
    elif numberrr % 3 == 0:
        print('fizz')
    elif numberrr % 5 == 0:
        print('buzz')
    else:
        print(numberrr)
