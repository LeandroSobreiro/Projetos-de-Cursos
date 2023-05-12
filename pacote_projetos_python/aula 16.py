a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)
# esse print conta qts vezes aparece o numero 5
print(c.count(5))

#mostra a posição que esta o numero 8
print(c.index(8))
print(len(c))
pessoa = ('Leandro', 35, 'M', 86.2)
# del(pessoa) apaga os todos os itens da tuplas
del(pessoa)
print(pessoa)