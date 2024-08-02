
numeros=[]
mai=0
men=0

for c in range(0,5):
    numeros.append(int(input(f'Digite um número para a posição {c}:   ')))
    if c == 0:
        mai = men = numeros[c]
    else:
        if numeros[c] > mai:
            mai = numeros[c]
        if numeros[c] < men:
            men = numeros[c]

print('-~-'*12)
print(f'Você digitou {numeros}')
print(f'O maior valor é {mai} na posição ', end='')
for i,v in enumerate(numeros):
    if v == mai:
        print(f'{i}')
print('\n')
print(f'O menor valor é {men} na posição ', end='')
for i,v in enumerate(numeros):
    if v == men:
        print(f'{i}')
print('\nAté mais!')