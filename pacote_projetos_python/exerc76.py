lista = ('Lápis', 2.50,'Caderno',8.00,'Estojo',4.30,'Bolsa',50.40,
         'Mesa',220,'Cadeira',120.5,'Computador',2.200,'Notebook',1250)
print('--'*20)
print('LISTAS DE PREÇOS')
print('--'*20)
#Para posicao em range de 0 ao comprimento da lista
for pos in range(0, len(lista)):
    # se posicao divisivel por 2 igual a 0
    if pos % 2 == 0:
        #imprime lista posicao pares alinhado a esquerda'<' 30 espacos
        print(f'{lista[pos]:.<30}',end='')
    else:
        #imprimir lista impares alinhado a direita '>' 7 espacos e com .2 casas depois do ponto
        print(f'R${lista[pos]:>7.2f}')
print('--'*20)