num =int(input('Digite um numero pra ver sua tabuada: '))
for c in range(1,11): # C e uma variavel que esta se repetindo entre 1 ate 11
    print('{} x {:2} = {}'.format(num,c,num*c))