from random import randint
while True:
        computador = randint(1, 11)
        jogador = int(input('Escolha um numero: '))
        total = computador + jogador
        tipo = ''
        tipo = str(input('Quer Par ou Impar[P/I]: ')).upper().strip()[0]
        while tipo not in 'PI':
                tipo = str(input('Quer Par ou Impar[P/I]: ')).upper().strip()[0]
        print(f'voce jogou {jogador} e o computador {computador} e o total foi {total}')
        if total % 2 == 0 and tipo == 'P':
                print('ganhou')
        if total % 2 == 1 and tipo == 'I':
                print('GANHOU')
        elif total % 2 == 0 and tipo == 'I' or total % 2 == 1 and tipo == 'P':
                print('PERDEU ....')
                break

