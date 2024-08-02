print(' --- JOGO DE DADOS ---')
import random as r
from operator import itemgetter
from time import sleep

jogador = {'Jogador um':r.randint(1,6),'Jogador dois':r.randint(1,6), 'Jogador três':r.randint(1,6),'Jogador quatro':r.randint(1,6)}
ranking = []
print()
for k,v in jogador.items():
    print(f'O {k} tirou o número {v}.')
    sleep(1)

print()
print(' ------ PLACAR ------')
print()
ranking = sorted(jogador.items(), key=itemgetter(1), reverse=True) # 0 ordena chave 1 ordena valor

for i,v in enumerate(ranking):
    print(f'{i+1}° lugar: {v[0]} com {v[1]} pontos.')
    sleep(0.5)