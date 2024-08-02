import random as r
from time import sleep

numeros = []


def sorteia(lista):
    print('Sorteando: ', end='')
    for c in range(0, 5):
        n = r.randint(1, 10)
        numeros.append(n)
        print(f'{n} ', end='', flush=True)
        sleep(0.5)
    print('Feito!')


sorteia(numeros)


def somapar(numeros):
    soma = 0
    for x in numeros:
        if x % 2 == 0:
            soma += x
    print(f'A soma de número pares é {soma}.')


somapar(numeros)    