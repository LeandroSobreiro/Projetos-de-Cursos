idade = 0
sexo = ''
resposta =''
maiorde18 = 0
mulhermenor = 0
totalh = 0
while True:
    print('-' * 20)
    print('CADASTRO DE PESSOAS')
    print('-' * 20)
    idade = int(input('Qual sua idade: '))
    sexo = str(input('Qual seu sexo (M/F): ')).upper().strip()[0]
    while sexo not in 'MF': # tem q ter a pergunta inicial para depois entrar no laco e repeti la ate a resposta for o que se pede M/F
        sexo = str(input('Qual seu sexo (M/F): ')).upper().strip()[0]# repete a pergunta q esta fora do laco pra ela entrar em loop caso seja errada a resp
    resposta = str(input('Quer continuar[S/N]')).upper().strip()[0]
    print('-' * 20)
    if sexo == 'M':
        totalh += 1
    if idade > 18:
        maiorde18 += 1
    if idade < 20 and sexo == 'F':
        mulhermenor += 1
    if resposta == 'N':
        break
print(f'No total fora cadastradas {maiorde18} maiores de 18 anos e {mulhermenor} mulher(es) menor de 20 anos !!!')
print(f'Total de homens cadrastrado {totalh} ')

