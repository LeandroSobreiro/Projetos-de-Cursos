listanum = []
while True:
    n = int(input('Digite um número: '))# crio uma variavel n normal
    if n not in listanum:# coloco se n nao esta em listanum
        listanum.append(n)# aki faco lista receber a variavel n cada vezes q acontece o loop
        print('Valor adicionado com Sucesso...')#ele escreve...
    else:
        print('Valor duplicado não vou adiionar...')
    resp = str(input('Quer continuar[S/N]')).upper().strip()
    if resp in 'Nn':
        break
print('-='*30)
listanum.sort()
print(f'Voce digitou os valores {listanum}')