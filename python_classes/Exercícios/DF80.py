valores = []
print('---- ', end='')
print('LISTA ORDENADA', end='')
print(' ----')

for c in range(0, 5):
    val = int(input('\nDigite um número:   '))
    if c == 0 or val > valores[-1]:
        valores.append(val)
        print('\nAdicionado ao final da lista!')
    else:
        pos = 0
        while pos < len(valores):
            if val <= valores[pos]:
                valores.insert(pos, val)
                print(f'\nAdicionado na posição {pos} da lista.')
                break
            pos += 1

print(f'Os valores digitados foram {valores}')