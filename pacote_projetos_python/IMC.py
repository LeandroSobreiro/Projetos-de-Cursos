peso = float(input('Qual seu peso KG: '))
alt = float(input('Qual sua altura : '))
imc = peso / (alt **2)
print('Sua massa corporea é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Esta abaixo do peso ideal')
elif imc <= 25:
    print('Voce esta no peso ideal')
elif  imc <= 30:
    print('Sobrepeso')
elif imc <= 40:
    print('Obesidade')
else:
    print('Obesidade Mórbita')