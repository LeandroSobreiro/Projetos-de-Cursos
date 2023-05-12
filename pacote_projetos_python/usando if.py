n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
m = (n1 + n2)/2
print('A sua media foi: {:.1f}'.format(m))
if m >= 6.0:
    print('Sua media foi boa!')
else:
    print('Sua media precisa melhorar !!')