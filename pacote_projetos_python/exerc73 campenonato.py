time = ('Corinthians','São Paulo','Palmeiras','Santos','Flamengo',
        'Fluminese','Curitiba','Vasco','Ponte Preta','Guarani')
print(f'Os cincos primeiros são {time [0:5]}')
print('-*-' * 20)
print(f'Os quatros ultimos são {time[-4:]}')
print('-*-' * 20)
print(f'Em ordem alfabetica são:{sorted(time)}')
print('-*-' * 20)
print(f'A Ponte Preta esta na posição: {time.index("Ponte Preta")}')