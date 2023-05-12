n = s = 0
while True:
    n = int(input('Digite um numero: '))
    if n == 999:
        break
    s = s + n
#print('A soma de todos os numero e {}'.format(s))
print(f'A soma de todos vale {s}')