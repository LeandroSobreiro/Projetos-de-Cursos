a = int(input('Digite o preimeiro numero: '))
b = int(input('Digite o segundo numero: '))
c = int(input('Digite o terceiro numero: '))
# verificando menor numero
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
#verificando o maior
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
print('O menor numero {}'.format(menor))
print('O maior numero {}'.format(maior))
