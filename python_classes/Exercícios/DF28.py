import random as r
num= r.randint(0,5)
esc=int(input('Escolha um número de 0 até 5:    '))
if esc== num:
    print('Prabéns! Você acertou!')
else:
    print('Você errou! O computador venceu.')
print('fim')