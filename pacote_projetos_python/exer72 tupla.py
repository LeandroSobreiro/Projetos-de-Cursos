cont = ('zero','um','dois','tres','quatro','cinco','seis',
        'sete','oito','nove','dez','onze','doze','treze',
        'quatroze','quinze','dezeseis','dezesete',
        'dezoito','dezenove','vinte')
while True:
    num = int(input('Digite um numero entre 0 e 20: '))
    if 0 <= num <=20:
        break
    print('Tente novamente ...')
print(f'O numero que voce digitou foi {cont[num]}')