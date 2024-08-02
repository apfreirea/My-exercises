print('--  ' * 4, end='')
print('LISTA', end='')
print('  --' * 4)
valores = []
r = ''
while True:
    if r != 'N':
        val = int(input('\nDigite um número:   '))
        valores.append(val)
        r = str(input('Deseja digitar mais um número? S/N')).upper()
        print('\n')
    else:
        break

print(f'Você digitou {len(valores)} números.')
valores.sort()
print(f'A lista de valores digitados foi {valores}')
if 5 in valores:
    print(f'O valor 5 foi digitado.')
else:
    print('Nenhum valor 5 foi digitado.')
print('Até mais!')