print()
def cab(a):
    print('-' * 30)
    print(f'{a:^30}')
    print(f'-' * 30)

def jogador():
    dados = []
    jogador = {}
    r = str(input('Cadastrar um jogador? S/N')).upper()
    while True:
        if r == 'S':
            jogador.clear()
            jogador['Nome'] = str(input('Nome do jogador: '))
            jogador['Gols'] = str(input('Número de Gols:  '))
            if jogador['Gols'].isnumeric():
                jogador['Gols'] = int(jogador['Gols'])
            else:
                jogador['Gols'] = 0
            dados.append(jogador.copy())
            r = str(input('Cadastrar outro jogador? S/N')).upper()
            print()
        else:
            break
    print(jogador)
    cab('FICHA DOS JOGADORES')
    print(f" {'Jogador:':^5} {'Gols:':^10}")
    for i in dados:
        print(f" {i['Nome']:^5} {i['Gols']:^14}")
    print('-' * 30)


print()
jogador()