a = float(input(' Quantos dias foi alugado o carro ? '))
km = float(input(' quantos km foi rodado ? '))
al = (60 * a) + (0.15 * km)
print(' O carro alugado por {} dias e rodado {} tem o custo de R$ {} '.format(a,km,al))
