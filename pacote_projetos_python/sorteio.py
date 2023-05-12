from random import choice
a1 = input('digite o primeiro aluno: ')
a2 = input('digite o segundo aluno: ')
a3 = input('digite o terceiro aluno: ')
a4 = input('digite o quarto aluno: ')
lista = [a1,a2,a3,a4]
escolhido = choice(lista)
print(' O aluno sorteado foi {}'.format(escolhido))