print('-' * 20)
print('LOJAS PARUDÃO')
print('-' * 20)
reposta = ''
preco = soma = acima = menor = cont =0
while True :
    produto = str(input('Nome do Produto: '))
    preco = int(input('Preço: '))
    resposta = str(input('Quer continuar [S/N]: ')).upper().strip()[0]
    print('-' * 20)
    soma = soma + preco
    cont += 1
    if cont == 1: # tem que criar um contador de produtos pra comparar
        menor = preco # se for so um produto ele se torna o mais barato
    else: # se nao for um so for mais entao continua
        if preco < menor or preco < menor:
            barato = produto # criar variavel pra receber o nome do produto mais barato
            menor = preco # uma variavel pra receber o valor do produto de menor valor
    if preco > 1000:
        acima += 1
    if resposta == 'N':
        break
print(f'O total  f'
      f''
      f'oi de R${soma} reais')
print(f'Temos {acima} custando mais de R$1000 Reais')
print(f'O produto mais barato foi {barato} que esta custando R${menor}')