v = float(input('Digite sua velocidade: '))
if v > 80:
    print('Multado : voce excedeu a velocidade permitida que é 80 km')
    m = (v - 80) * 7
    print('Voce pagara uma multa de R$: {:.2f}'.format(m))
print(' Boa viajem!!!')