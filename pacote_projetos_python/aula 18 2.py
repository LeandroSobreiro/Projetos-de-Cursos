teste = list()# lista normal
teste.append('Leandro')# recebe leandro na posicao 0
teste.append(35)#recebe 35 posicao 1
galera = []# galera inicialmente lista normal, mais ao colocar mais itens se torna composta
galera.append(teste[:])# galera vai receber a lista teste o [:] significa copia
teste[0] = 'Maria'# teste na posicao 0 vai receber maria
teste[1] = 22# teste na posicao 1 ..22
galera.append(teste[:])# galera agora recebe mais um item na lista
print(galera)

galera = [['Joao',19],['Ana',33],['Joaquim',13],['Maria',45]]
for p in galera:
    #print(p[0])# imprime todos os dados da posicao 0 de cada bloco que aki sao os nomes
    #print(p[1])# imprime todos os dados da posicao 1 de cada bloco que sao idades
    print(f'{p[0]} tem {p[1]} anos de idade ')
print('--'*18)
print(galera[0])
print(galera[0][0])
print(galera[1][0])