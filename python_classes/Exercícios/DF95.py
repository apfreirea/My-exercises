print('==== AVALIAÇÃO DE DESEMPENHO ====')
print()

desempenho = []

jogador = {}
print(' ------ CADASTRO DO JOGADOR ------')
r = str(input('\nDeseja cadastrar um jogador? S/N\n')).upper()[0]
while True:
    if r == 'S':
        jogador.clear()
        jogador['Jogador']=str(input('Nome do jogador:  '))
        jogador['Partidas']=int(input('Quantas partidas jogou?  '))
        jogador['Gol']= 0
        for p in range(0,jogador['Partidas']):
                g=int(input(f'Número de gols da {p+1}°Partida: '))
                jogador['Gol'] += g
        jogador['Campeonato']=jogador['Partidas']*jogador['Gol']
        desempenho.append(jogador.copy())
        r = str(input('Deseja cadastrar outro jogador? S/N')).upper()[0]
    elif r == 'N':
        break
# print('-'*36)
# for i in desempenho:
    # print(f"O jogador {i['Jogador']} relizou {i['Gol']} gols em {i['Partidas']} partidas durante o campeonato.")
# print('-'*36)
print()
print('-'*36)
print(f'{"TIME":^36}')
print('-'*36)


print(f'{"JOGADOR":^4}  {"PARTIDAS":^10}  {"GOLS":^13}')
for i in desempenho:
    print(f"{i['Jogador']:^4}   {i['Partidas']:^11}  {i['Gol']:^13}")
print()
print('-'*36)