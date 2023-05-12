num = [2,5,9,1]
num[2] = 3 # trocar um numero da lista
num.append(7)# adicionar um numero na lista
num.sort()# ordena em ordem crescente
num.sort(reverse=True)# oredena em ordem reversa
num.insert(2,2)# adiciona o numero zero na posicao dois
num.remove(2)# o remove remove elemento declarado e sempre o primeiro da esquerda pra direita
if 4 in num:# se nao tiver o elemento 4 ele nao da erro
    num.remove(4)# da a msg do else
else:
    print('Nao achei o numero 4')
if 5 in num:# qd se tem o elemento entao ele apaga
    num.remove(5)
else:
    print('Nao achei o numero 4')
#num.pop(2)# remove o elemento selecionado posicao 2 nesse caso ou se nao colocar posicao sera o ultimo
print(num)
print(f'Esta lista tem {len(num)} elementos')