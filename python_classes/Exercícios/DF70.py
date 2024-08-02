gasto = []
cont = 0
lista = []

print('LISTA DE COMPRAS')

while True:
    prod = str(input('\nNome do produto:  ')).capitalize()
    lista.append(prod)
    preco = float(input('Quanto custa? '))
    gasto.append(preco)

    if preco > 1000:
        cont += 1

    ttl = sum(gasto)
    add = str(input('\nGostaria de adicionar outro produto? S/N')).upper()
    if add == 'S':
        prod = str(input('\nNome do produto:  ')).capitalize()
        lista.append(prod)
        preco = float(input('Quanto custou? '))
        gasto.append(preco)

        if preco > 1000:
            cont += 1

        ttl = sum(gasto)
        add = str(input('\nGostaria de adicionar outro produto? S/N')).upper()
    elif add == 'N':
        print('FIM DO PROGRAMA')
        break
    elif add != 'S' or add != 'N':
        print('Resposta inválida!')
        add = str(input('\nGostaria de adicionar outro produto? S/N')).upper()




minimo = min(gasto)
barato = gasto.index(minimo)
nome = lista[barato]
print(f'\nO total da compra foi R${ttl:.2f}. ')
print(f'{cont} produtos custaram mais que R$1000.')
print(f'O produto mais barato foi {nome} por R${minimo:.2f}.')