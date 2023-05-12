resp = 'S'
soma = quant = media = maior = menor= 0
while resp in 'Ss':
    n1 = int(input('Digite um numero: '))
    soma += n1
    quant += 1
    if quant == 1:
        maior = menor = n1
    else:
        if n1 > maior:
            maior = n1
        if n1 < menor:
            menor = n1
    resp = str(input('Quer continuar [S/N] ')).upper().strip()[0]
media = soma / quant
print('voce digitou {} numeros e a media foi {}'.format(quant,media))
print(' O maior valor foi {} e o menor foi {} '.format(maior,menor))