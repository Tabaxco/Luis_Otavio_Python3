macaco = range(11)

for c in macaco:
    print(c, end='\n')
    print(macaco[5], end= '\t')

for numero in macaco:
    print(numero)

### Não precisa se preocupar com indíces, o range já faz isso para você.
### Preciso me preocupar com valores.

jonas = 'jonas'.__iter__()
print(jonas)