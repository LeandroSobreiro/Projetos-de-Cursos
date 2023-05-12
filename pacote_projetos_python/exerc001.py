casa = float(input('Valor da casa ? '))
salario = float(input('Qual é seu salario ? '))
anos = int(input('Em qunatos anos pretende pagar ? '))
prestacao = casa /(anos * 12)
minimo = salario * 30/100
aprovado = (1 + salario) - (salario * 30/100)
print('Para pagar uma casa de R${:.2f} em {} anos'.format(casa,anos),end='')
print('a prestação será de R${:.2f}'.format(prestacao))
if prestacao <= minimo:
    print('Emprestimo pode ser CONCEDIDO')
else:
    print('Emprestimo NEGADO')