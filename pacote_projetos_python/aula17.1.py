valores =list()
#valores.append(5)
#valores.append(9)
#valores.append(4)
for cont in range(0,5):
    valores.append(int(input('Digite um numero: ')))
for c,v in enumerate(valores): # para c,em v enumerar valores c seria o indice e valores os dados da lista
    print(f'Na posição {c} encontrei o valor {v}')
print('Cheguei ao final da lista. ')
'''a = [ 2,3,4,7]
b = a[:]# assim b recebe uma copia de a que pode ser mudado [:] = copia de td
b[2] = 8  # se for a = b assim altera tanto a lista B e a A por estarem ligadas
print(f'Lista A: {a}')
print(f'Lista B: {b}')'''