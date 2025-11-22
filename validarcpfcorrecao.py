cpf = '74682489070'
nove_digitos = cpf[:9]
contador_regressivos1 = 10

resultado1 = 0

for digito in nove_digitos:
    resultado1 += int(digito) * contador_regressivo1
    contador_regressivo1 -= 1

digito1 = (resultado1 * 10) % 11

digito1 = digito1 if digito1 <= 9 else 0
print(digito) 