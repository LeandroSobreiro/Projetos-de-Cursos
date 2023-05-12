from time import sleep
n1 = int(input('Primeiro numero: '))
n2 = int(input('Segundo numero: '))
opcao = 0 # se for tipo str a variavel vai ser igual a ' '
while opcao != 5:
    print('''    [1] SOMA 
    [2]MULTIPLICA
    [3]MAIOR
    [4]NOVOS NUMEROS
    [5]SAIR DO PROGRAMA''')# um print com tres aspas permite imprimir pulando linha 
    opcao = int(input('Qual é sua opção: '))# se colocar uma variavl aki tem que ter outra variavel com valor 0 fora do laco
    if opcao == 1:
        print('A soma de {} e {} é {}'.format(n1,n2,n1+n2))
    elif opcao == 2:
        print('A multiplicação do numero {} e {} o numero teve resultado {}'.format(n1,n2,n1*n2))
    elif opcao == 3:
        if n1 > n2:
            print('O maior numero é {}'.format(n1))
        else:
            print('O maior numero é {}'.format(n2))
    elif opcao == 4:
            print('Digite de novo os numeros')
            n1 = int(input('Primeiro numero: '))
            n2 = int(input('Segundo numero: '))
    elif opcao == 5:
        print('FINALIZANDO...')
    else:
        print('Opção invalida tente novamente')
sleep(1)
print('Programa finalizado, volte sempre!!!')