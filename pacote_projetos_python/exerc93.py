dados = {}
partidas = list()
dados['nome'] = str(input('Nome do Jogador: '))
tot = int(input(f'Quantas partidas {dados["nome"]} jogou: '))
for c in range(0,tot):
    partidas.append(int(input(f'Quantos gols na partida {c}?  ')))
dados['gols'] = partidas[:]# dados gol vai receber a copia da lista partidas
dados['total'] = sum(partidas)#dados total vai receber a soma dos dados da lista partida usando(sum)
print('-='*30)
print(dados)
print('-='*30)
for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*30)
print(f'O jogador {dados["nome"]} jogou {len("gols")} partidas')
for i, v in enumerate(dados['gols']):
    print(f'  => Na partida {i}, fez {v} gols.')
print(f'Foi um total de {dados["total"]} gols.')