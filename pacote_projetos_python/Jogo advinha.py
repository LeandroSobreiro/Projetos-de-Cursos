from random import randint # biblioteca pra escolher um numero sozinho
from time import sleep  # bilioteca pra tempo no caso espera..
computador = randint(0,5)# Faz o computador pensar num numero
print('-=-' * 20)
print('Vou pensar em um numero...')
print('-=-'*20)
Jogador = int(input('Digite um numero de 0 a 5: '))
print('PROCESSAnDO...')
sleep(2)# tempo de espera
if Jogador == computador:
    print('Voce acerto miseravi !!!')
else:
    print('Eu pensei no numero {} e nao no {}'.format(computador,Jogador))