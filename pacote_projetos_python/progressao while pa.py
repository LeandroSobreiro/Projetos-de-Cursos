print('Contador de PA')
print('-='*10)
primeiro = int(input('Digite o termo: '))
razao = int(input('Digite a razao: '))
termo = primeiro
c = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while c <= total:
        print('{} -> '.format(termo),end='')
        termo += razao
        c += 1
    print('PAUSA')
    mais = int(input('Quantos termos a mais voce quer mostrar: '))
print('Progressão finalizada com {} termos'.format(total))