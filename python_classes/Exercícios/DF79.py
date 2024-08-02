valores = []
asw = ''
while True:
    if asw != 'N':
        val = int(input('\nDigite um valor:   '))
        if val in valores:
            print('Esse número já existe!')
            asw = str(input('\nQuer continuar? S/N')).upper()
        else:
            valores.append(val)
            asw = str(input('\nQuer continuar? S/N')).upper()

    else:
        break

print('--' * 10)
valores.sort()
print(f'Os valores digitados foram {valores}.')