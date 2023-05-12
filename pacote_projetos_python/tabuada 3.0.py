while True:
    print(''* 20)
    tab = int(input('Quer ver a tabuada de qual numero: '))
    if tab < 0:
        break
    for n in range(1,11):
        print(f'{tab} x {n} = {tab * n}')
print('Programa encerrado volte sempre!!!')
