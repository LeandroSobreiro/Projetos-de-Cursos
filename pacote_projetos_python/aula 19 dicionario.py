pessoas = {'nome':'Leandro','sexo': 'M','idade': 35}
pessoas['nome'] = 'Dulcinea' # modificar o nome ja declarado
pessoas['peso'] = 86 # adicionar novo valor no dicionario
for k,v in pessoas.items():
    print(f'{k} = {v}')# k significa keys = nome,sexo,idade e v values = Leandro,m,35

print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())