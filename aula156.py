try:
    import sys
    sys.path.append('/home')
except ModuleNotFoundError:
    ...
import aula155

print('Este módulo se chama', __name__)

print(aula155.jonas)
print(*sys.path, sep = '\n')