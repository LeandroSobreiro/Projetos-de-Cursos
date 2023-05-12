from _datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}'.format(nasc,idade,atual))
if idade > 18:
    print('Voce deveria ter se alistado antes')
elif idade < 18:
    saldo = 18 - idade
    print('Falta {} anos pra você se alistar'.format(saldo))
elif idade == 18:
    print('Nesse ano voce deve se alistar ou ja se alistou ')