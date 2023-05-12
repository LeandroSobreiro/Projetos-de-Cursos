lanche = ('Hamburger', 'Suco','Pizza','Pudim','Batata frita')

# usando print com sorted ele coloca em ordem alfabetica
print(sorted(lanche))

# alem de imprimir pode inumuera cada item
for cont in range(0,len(lanche)):
    print(f'Eu comi {lanche[cont]} na posição {cont}')

# pos, comida sao duas variaveis por isso a , separando
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')

for comida in lanche:
    print(f'Eu vou comer {comida}')

print('Comi pra caramba!')
#print(len(lanche)) # conta conts itens tem na variavel. dividido por virgula e ''
#tuplas sao imutaveis
#print(lanche)
#print(lanche[:2])