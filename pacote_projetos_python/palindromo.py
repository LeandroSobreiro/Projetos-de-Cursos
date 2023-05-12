frase = str(input('Digite uma frase: ')).strip().upper()
palavra = frase.split()
junto = ''.join(palavra)
inverso = junto[:: -1]
print('Voce digitou a frase {}'.format(junto))
'''for letra in range(len(junto) -1,-1,-1):
    inverso += junto[letra]'''
if inverso == junto:
    print('A frase é um palindromo')
else:
    print('A frase NÃO é um palindromo')