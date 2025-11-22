jonas = {'jonas' : 1, 'joão' : 2, 'jose' : 3}


for i in jonas:
    print(f'{i} : {jonas[i]}')

jonas = {
    'grupo1' : {'macacoide' : 1, 'macacoide2' : 2},
    'grupo2' : {'macacoide3' : 3, 'macacoide4': 4},
}

print(jonas['grupo1']['macacoide'])