import random as r

print('JOGO DO PAR OU ÍMPAR')
print('- - ' * 5)
cont = 0
while True:
    esc = str(input('Você deseja PAR ou ÍMPAR? ')).upper()
    num = int(input('Escolha um número:  '))
    comp = r.randint(0, 10)
    print(f'O computador escolheu {comp}.')
    print(f'A soma de {num} + {comp} = {num + comp}')
    if esc == 'PAR' and (num + comp) % 2 == 0:
        print('Parabéns! Você venceu!')
        cont += 1
        print(f'Você obtve {cont} vitórias até aqui.')
    elif esc == 'PAR' and (num + comp) % 2 != 0:
        print('GAME OVER!')
        print(f'Você obtve {cont} vitórias até aqui.')
        break
    elif esc == 'IMPAR' and (num + comp) % 2 != 0:
        print('Parabéns! Você venceu!')
        cont += 1
        print(f'Você obtve {cont} vitórias até aqui.')
    elif esc == 'IMPAR' and (num + comp) % 2 == 0:
        print('GAME OVER!')
        print(f'Você obtve {cont} vitórias até aqui.')
        break
    print(' \n \n ')

print('Até mais!')
