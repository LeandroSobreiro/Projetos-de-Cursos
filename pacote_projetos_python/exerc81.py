listanum = []
resp = ''
while True:
    listanum.append(int(input('Digite um numero: ')))
    resp = str(input('Quer continuar [S/N]')).upper().strip()[0]
    if resp in 'Nn':
        break
print(f'Voce digitous {len(listanum)} elementos')
listanum.sort(reverse=True)
print(f'Os valores digitados em ordem decrescente foi {listanum}')
if 5 in listanum:
    print('O valor 5 faz parte da lista')
else:
    print('Não achei nenhum valor 5 na lista')