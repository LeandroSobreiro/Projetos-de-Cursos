galera = []
dados = []
maior = menor = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Peso: ')))
    if len(galera) == 0:
        maior = menor = dados[1]
    else:
        if dados[1]> maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    galera.append(dados[:])
    dados.clear()
    rsp = str(input('Quer continuar [S/N]: ')).upper()
    if rsp in 'Nn':
        break
print('-*' * 14)
print(f'Ao todo foram cadastrados {len(galera)} pessoas')
print(f'O maior peso foi de {maior}kg de ', end='')
for p in galera:
    if p[1] == maior:
        print(f'[{p[0]}]', end='')
print()
print(f'O menor peso foi de {menor}kg de ', end='')
for p in galera:
    if p[1] == menor:
        print(f'[{p[0]}]', end='')