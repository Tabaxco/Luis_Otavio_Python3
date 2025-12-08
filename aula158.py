import aula158m
import importlib

print(aula158m.variavel)

for i in range(10):
    importlib.reload(aula158m)
    print(i)

print('Fim')