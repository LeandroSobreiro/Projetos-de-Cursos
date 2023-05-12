n = s = q = 0
while True:
    n = int(input('Digite um numero[para parar digite 999]: '))
    if n == 999:
        break
    s += n
    q += 1
print(f'Foram digitados {q} numeros e sua soma foi {s}')