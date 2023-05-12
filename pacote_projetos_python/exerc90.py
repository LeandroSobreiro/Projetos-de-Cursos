aluno = {}
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Media de {aluno["nome"]}: '))
if aluno['media'] >= 7:
    aluno['situacao'] = 'Aprovado'
elif 5 < aluno['media'] < 7:
    aluno['situacao'] = 'Recuperação'
elif aluno['media'] < 5:
    aluno['situacao'] = 'Reprovado'
print('-='*30)
# para cada k chave [nome,media,situacao], v valores igual o nome digitado e media digitada
#ja a situacao vai depender da media  onde ... aluno{nome: leandro , media: 9 , situacao: 9 no caso} tudo igual a item89
#                                                      { k     v         k    v     k       v    } = alun.items()
for k, v in aluno.items():
    print(f'{k} é igual a {v}')
