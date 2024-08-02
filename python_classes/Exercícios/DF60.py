import numpy as n

# numpy prod multiplica todos os valores dentro da lista
num=int(input('Escolha um número:   '))
print('O número escolhido foi {}, certo?!'.format(num))
fac=[]

for numeros in range(num-1,0,-1):
    fac.append(numeros)
    produto=n.prod(fac)
    resultado=num*produto
print(resultado)