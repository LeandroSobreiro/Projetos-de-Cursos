primeiro = int(input('Digite um termo: '))
razao = int(input('Digite a razão: '))
decimo = primeiro + (10 -1) * razao
for c in range(primeiro,decimo,razao):
    print('{} '.format(c),end='-> ')
print('ACABOU')