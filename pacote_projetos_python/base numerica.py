num = int(input('Digite um numero inteiro: '))
print('''Escolha a base de conversão:
[1] Converte para BINÁRIO
[2] Converte para OCTAL
[3] Converte para HÉXADECIMAL''')
opção = int(input('Sua opção: '))
if opção == 1:
    print('{} convertido em Binário é {} '.format(num,bin(num)[2:]))
elif opção == 2:
    print('{} convertido em Octal é {}'.format(num,oct(num)[2:]))
elif opção == 3:
    print('{} convertido em Hexadecimal é {}'.format(num,hex(num)[2:]))
else :
    print('Opção invalida tente novamente ')