d = float(input('Digite quantos KM tem sua viajem!!! '))
print(' voce ira comecar uma vijem e {} KM'.format(d))
if d <= 200:
    c1 = d * 0.50
    print(' Sua viajem ira custar R$ {}'.format(c1))
else:
    c2 = d * 0.45
    print('Sua viajem custara R$ {} '.format(c2))