from random import randint
num = ( randint(0,20),randint(0,20),randint(0,20),
        randint(0,20),randint(0,20),randint(0,20))
for n in num:
    print(n ,end=' ')
print(f'\nO maior numero foi {max(num)}')


print(f'O menor foi {min(num)}')

produto = ('Mesa',550.40,'Cadeira', 43,'Prato',10.70,'Copo',3.75)
print('-+-'*5)
print('Produtos')
print('-+-'*5)
for pos in range(0,len(produto)):
    if pos % 2 == 0:
        print(f'{produto[pos]:.<20}',end='')
    else:
        print(f'R$ {produto[pos]:.>4.2f}')

palavra = ('Dulcinea','Leandro','Theo',
           'Fernanda','Thor')
for p in palavra:
    print(f'\nOs nomes aqui sao {p} as vogais são: ',end='')
    for letras in p:
        if letras in 'aeiou':
            print(letras,end='')

