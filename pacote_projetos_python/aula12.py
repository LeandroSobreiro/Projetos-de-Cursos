nome = str(input('Qual seu nome ? '))
if nome == 'Leandro':
    print('Que nome lindo !!!')
elif nome == 'Fernanda' or nome == 'Maria' or nome == 'Dulci':
    print('Seu nome esta na familia !!')
elif nome in 'Rafaela Claudia Juliana':
    print('Seu nome é igual ao da minha irmã !!')
else:
    print('Seu nome é bem normal ...')
print('Tenha um bom dia , {} !!!'.format(nome))