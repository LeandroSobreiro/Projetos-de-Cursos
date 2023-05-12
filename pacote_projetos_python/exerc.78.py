num = list()
maior = 0
menor = 0
for c in range(0,5):# c e uma valriavel que conta as posicoes
    num.append(int(input(f'Digite um numero para a posicao {c}: ')))# um input com f' pode se colocar uma variavel
    if c == 0:
        maior = menor = num[c]
    else:
        if num[c] > maior:
            maior = num[c]
        if num[c] < menor:
            menor = num[c]
print('-='*30)
print(f'Voce digitou os valores: {num}')
print('-='*30)
print(f'O maior numero encontrado foi {maior}  na posição ',end='')
for i, v in enumerate(num):# i representa indice ou posicao v valor ou o numero
    if v == maior:
        print(f'{i}...',end='')
print(f'\nO menor valor encontrado foi {menor} na posição ',end='')
for i, v in enumerate(num):
    if v == menor:
        print(f'{i}...',end='')
print()
