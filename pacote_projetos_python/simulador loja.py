print('{:=^40}'.format(' Lojas Parudão '))
produto = float(input('Digite o valor de suas compras: R$ '))
desc = produto - (produto * 10 / 100)
desc1 = produto - (produto * 5 / 100)
normal = produto / 2
juros = produto + (produto * 20/100)
parcela = juros / 3
print('''Qual a opção de pagamento:
[1] a vista: dinheiro ou cheque:
[2] a vista : cartão: 5% de desconto
[3] em ate 2x no cartão: preço normal
[4] 3x ou mais no cartão : 20% de juros''')
opcao = int(input('Qual sua opção: '))
if opcao == 1:
    print('Voce ira pagar R$: {}'.format(desc))
elif opcao ==2:
    print('Voce ira pagar R$:{} '.format(desc1))
elif opcao == 3:
    print('Voce ira pagar R$ {} ou em 2x de R$:{}'.format(produto,normal))
elif opcao == 4:
    print('Voce ira pagar um total de R$: {} em ate 3x de R$: {}'.format(juros,parcela))
else:
    print('Opção invalida')