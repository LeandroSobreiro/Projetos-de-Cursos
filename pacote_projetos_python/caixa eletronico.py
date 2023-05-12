quant50 = notas10 = notas50 = quant10 = quant5 = notas5 = 0
saque = int(input('Qual o valor do saque R$: '))
while True:
    if saque / 50 :
        notas50 = saque // 50
    if saque / 10:
        notas10 = saque % 50
        quant10 = notas10 // 10
    if saque / 5:
        notas5 = notas10 % 10
        quant5 = notas5 // 5
    break
print(f'''Seu que vai ter: 
{notas50} notas de R$: 50 reais 
{quant10} notas de R$: 10 reais 
{quant5}  notas de R$: 5 reais''')
