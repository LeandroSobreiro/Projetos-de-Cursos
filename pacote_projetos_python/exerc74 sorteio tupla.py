from random import randint
maior = 0
numeros = (randint(0, 10),randint(0, 10),randint(0, 10),
randint(0, 10),randint(0, 10))
print(f'Os números sorteados foram:',end='')
for n in numeros:
    print(f' {n} ',end='')
# \n usado pra imprimir na linha debaixo e max busca o valor maximo em numeros
print(f'\nO maior valor sorteado foi: {max(numeros)}')
# min busca o valor minimo na lista numeros
print(f'O menor valor sorteado foi: {min(numeros)}')