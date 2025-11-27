
i = 5
def escopo():
    for j in range(5):
        i += 1
        print(i)
        print('jonas')
    x = 1
    print(x)

escopo()