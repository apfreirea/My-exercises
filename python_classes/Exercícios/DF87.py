print(' - - - MATRIZ - - - ')

c1 = []
c2 = []
c3 = []

for um in range(0, 3):
    v1 = int(input(f'Digite o valor {um} da linha 1:  '))
    c1.append(v1)

print('\n')
for dois in range(0, 3):
    v2 = int(input(f'Digite o valor {dois} da linha 2:  '))
    c2.append(v2)

print('\n')
for tres in range(0, 3):
    v3 = int(input(f'Digite o valor {dois} da linha 3:  '))
    c3.append(v3)

print('\n')
print(' - - - MATRIZ 3X3 - - -')
for a, b, c in c1, c2, c3:
    print(f'\t {a} {b} {c}')
print(' - - - - - - - - - - - ')

print(f'\nItem A: a soma de todos os valores ', end='')
soma = sum(c1) + sum(c2) + sum(c3)
print(soma)
print(f'Item B: a soma da Coluna 3 é ', end='')
print(f'{c1[2]} + {c2[2]} + {c3[2]} = {c1[2] + c2[2] + c3[2]}.')
print(f'Item C: o maior valor da segunda linha é {max(c2)}.')