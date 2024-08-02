num = list()
for cont in range(0, 5):
    num.append(int(input('Digite um valor:  ')))

print(f'\nLista: {num}')

for c, n in enumerate(num):
    print(f'Na posição {c} encontramos {n}')
    nummm = max(num)
    indmax = num.index(nummm)
    nummin = min(num)
    indmin = num.index(nummin)
print(f'\nO maior valor for {nummm} e está na posição {indmax}.')
print(f'O menor valor foi {nummin} e está na posição {indmin}.')