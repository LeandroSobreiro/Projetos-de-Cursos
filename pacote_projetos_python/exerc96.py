def area(larg,comp):
    a = larg * comp
    print(f'A area de um terreno { larg} x {comp} tem a area {a} m²')


#programa principal
print('Controle de Terrenos ')
print('-'*20)
l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))
area(l,c)