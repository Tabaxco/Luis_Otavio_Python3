from sys import path
import aula159_package.modulo
# aula159_package.modulo import soma_do_modulo
from aula159_package import modulo
from aula159_package.modulo import *

#print(*path, sep = '\n')
print(soma_do_modulo(9, 3))
print(aula159_package.modulo.soma_do_modulo(9, 3))
print(modulo.soma_do_modulo(9, 3))
print(variavel)