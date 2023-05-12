def soma(a,b):
    print(f' A = {a} e B = {b}')
    s = a + b
    print(f'A soma A + B = {s}')


#programa principal
soma(b=4, a=5)
soma(a=8, b=9)
# se nao explicitar o primeiro sera no caso a =2 e b= 3
soma(2, 1)

def contador(* num):
    #for valor in num:
     #   print(f'{valor} ',end='')
    #print('FIM')
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} numeros')

#programa principal
contador(2,1,7)
contador(8,0)
contador(4,4,7,6,2)
