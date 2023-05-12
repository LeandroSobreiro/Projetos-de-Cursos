r1 = int(input('Segmento 1: '))
r2 = int(input('Segmento 2: '))
r3 = int(input('Segmento 3: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print(' Os segmentos PODEM forma um triângulo !!!')
    if r1 ==r2 and r2 == r3:
        print('Equilatero')
    if r1 !=r2 != r3 != r1:
        print('Escaleno')
    else:
        print('Isósceles')
else:
    print('Os segmentos NÃO PODEM formar um triângulo !!')