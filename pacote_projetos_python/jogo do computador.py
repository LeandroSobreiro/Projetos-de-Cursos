from random import randint
computador = randint(0, 10)
usuario = 11
soma = 0
print('Olá sou seu computador Pensei em um numero entre 0 e 10')
while computador != usuario:
    if computador != usuario:
        usuario = int(input('Digite um numero de 0 a 10: '))
        soma += 1
print(' O computador  penseu no numero {} e voce acertou em {} tentativas!!!'.format(computador,soma))
print('Parabens')