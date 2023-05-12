num = [[],[]]
dado = 0
for c in range(0,7):
    dado = int(input(f'Digite o {c + 1} valor: '))
    if dado % 2 == 0:
        num[0].append(dado)
    else:
        num[1].append(dado)
num[0].sort()
num[1].sort()
print(f'Os valores pares foram: {num[0]}')
print(f'Os valores impares foram: {num[1]}')