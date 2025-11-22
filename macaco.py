macaquice = 0

while True:
    macaquice +=1

    for c in range(macaquice):
        print('Macaco infinito')

        if macaquice >= 1000:
            print('Macaco finito...')
            break
        
        if macaquice >= 200:
            print(macaquice)
        else:
            continue