exp = str(input('Digite uma expresão: '))
pilha = []
for simb in exp:
    if simb == '(':
        pilha.append('(')
    elif simb ==')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressã0 é valida !!!')
else:
    print('Expresão invalida')