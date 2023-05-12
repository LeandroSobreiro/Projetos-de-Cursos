salario = float(input(' Qual seu salario ? R$ '))
aumento = salario + (salario * 11.08 / 100)
print(' O salario de R$ {} com 15 % de aumento passa a ser R$ {:.2f} '.format(salario,aumento))