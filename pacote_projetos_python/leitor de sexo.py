sexo = str(input('Informe seu sexo: [M/F] ')).upper().strip()[0]
while sexo not in 'MF':
    sexo = str(input('invalido digite novamente: ')).upper().strip()[0]
print('sua opção foi salva com Sucesso')