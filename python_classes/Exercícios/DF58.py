import random as r

num = r.randint(0,10)
jogador=int(input('Digite um número entre 0 e 10:  '))
tentativas=0
while jogador is not num:
    print('Resposta errada!')
    jogador=int(input('Digite um número entre 0 e 10:  '))
    if jogador != num:
        tentativas += 1

print('Você acertou!')
print('Foram necessárias {} tentativas.'.format(tentativas))