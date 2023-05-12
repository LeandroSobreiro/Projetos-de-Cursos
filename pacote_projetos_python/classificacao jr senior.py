from datetime import date
atual = date.today().year
nasc = int(input('Digite o ano do seu nascimento: '))
idade = atual - nasc
print('Sua idade é {}'.format(idade))
if idade <= 9:
    print('Voce é um atleta MIRIM')
elif idade <= 14:
    print('Voce é um atleta INFANTIL')
elif idade <= 19:
    print('Voce é um atleta JUNIOR')
elif idade <= 25:
    print('Voce é um atleta SÊNIOR')
else:
    print('Voce é uma atleta MASTER')
