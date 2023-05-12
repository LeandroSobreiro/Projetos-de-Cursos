primeiro = int(input('Digite um termo: '))
razao = int(input('Digite a razao: '))
termo = primeiro
c = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while c <= total:
        print('{}'.format(termo), end=' ')
        termo += razao
        c += 1
    print('Pausa')
    mais = int(input('Quantos mais voce quer ver: '))
print('fim total de {}'.format(total))