resp = ''
soma = maior = menor = quant = 0
while resp in 'Ss':
    num = int(input('Digite um numero: '))
    resp = str(input('Quer continuar [S/N]')).upper().strip()[0]
    soma += num
    quant += 1
    if quant == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num
print(' O maior numero foi {} e o menor {}'.format(maior,menor))
print('E a soma desses numeros e de {}'.format(soma))