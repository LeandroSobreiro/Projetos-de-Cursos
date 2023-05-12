nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media =(nota1 + nota2) / 2
print('Sua nota foi {}'.format(media))
if media > 7:
    print('Sua média foi {} e você está APROVADO')
elif media < 5:
    print('Você esta REPROVADO')
elif media > 5.0 < 6.9:
    print('Você esta de RECUPERAÇÃO' )
