cont = 0
continuar = ''
valor = 0
produto = ''
produtocaro = ''
produtobarato = ''
maiscaro = 0
total = 0
maisbarato = 0
print('+'*20)
print('Lojao do Leandro')
print('+'*20)
while True:
    produto = str(input('Escolha um produto: '))
    valor = int(input('Qual valor do produto: '))
    continuar = str(input('Quer continuar(S/N): ')).upper()
    print('\n')
    cont += 1
    total += valor
    if cont == 1:
        maiscaro = valor
        maisbarato = valor
        produtocaro = produto
        produtobarato = produto
    if valor > maiscaro:
        maiscaro = valor
        produtocaro = produto
    if valor < maisbarato:
        maisbarato = valor
        produtobarato = produto
    if continuar == 'N':
        break
print(f'''O produto mais caro foi {produtocaro} e custou R$:{maiscaro}
O produto mais barato foi {produtobarato } e custou R$:{maisbarato}
total deu R$:{total}''')
