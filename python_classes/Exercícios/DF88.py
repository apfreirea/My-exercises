import random as r
print('    MEGA SENA     \n')

game = []
jogos = int(input('Quantos jogos irá fazer? R:'))


print('\n--- Criando Jogos ---')
for j in range(0,jogos):
    j1=(r.randint(1,60),r.randint(1,60),r.randint(1,60),r.randint(1,60),r.randint(1,60),r.randint(1,60))
    game.append(j1)
    print(f'\nJogo {j} {j1}')