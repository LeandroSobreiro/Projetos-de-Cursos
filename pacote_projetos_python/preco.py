q = float(input('Qual o preco do produto ? R$  '))
v = q - (q * 5 / 100)
print(' O produto que custava R$ {}, agora com 5% desconto esta R$ {:.2f} '.format(q,v))