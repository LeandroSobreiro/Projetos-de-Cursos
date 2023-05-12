galera = list()
dado = list()
totmai = 0
totmen = 0
for c in range(0,3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])#[:] significa copia de dado
    dado.clear()
for p in galera:
    if p[1]> 21:
        totmai += 1
        print(f'{p[0]} é maior de idade.')
    else:
        totmen += 1
        print(f'{p[0]} é menor de idade.')
print(f'Temos {totmai} maior de idade e temos {totmen} menor de idade')