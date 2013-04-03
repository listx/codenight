answer = 0

for numba in range(1,1000):
    if (numba % 3 == 0):
        answer += numba
    elif (numba % 5 == 0):
        answer += numba

print(answer)
