pessoa = list()
dado = list()
pesado = leve = 0
r = str(input('Deseja cadastrar alguém? S/N')).upper()
while True:
    if r == 'S':
        dado.append(str(input('\nNome:   ')))
        dado.append(float(input('Peso:   ')))
        if len(pessoa) == 0:
            pesado = leve = dado[1]
        else:
            if dado[1] > pesado:
                pesado = dado[1]
            if dado[1] < leve:
                leve = dado[1]
        pessoa.append(dado[:])
        dado.clear()
        r = str(input('Deseja cadastrar mais alguém? S/N')).upper()
    else:
        break
print(f'\nForam cadastradas {len(pessoa)} pessoas.')
for p in pessoa:
    print(f'{p[0]} pesa {p[1]} kg.')
print(f'\nA pessoa com maior peso tem {pesado} kg e é', end=' ')
for p in pessoa:
    if p[1] == pesado:
        print(f'{p[0]}')
print(f'A pessoa com menor peso tem {leve} kg e é', end=' ')
for p in pessoa:
    if p[1] == leve:
        print(f'{p[0]}')
