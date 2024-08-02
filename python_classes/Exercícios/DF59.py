import random as r

n1 = int(input('Escolha um número:   '))
n2 = int(input('Escolha um número:   '))
print('Os números escolhidos são {} e {}.'.format(n1, n2))

print('MENU \n \n [1] Somar \n [2] Multiplicar \n [3] Maior \n [4] Novos números \n [5] Sair do progr0ama')
escolha = 0
while escolha != 5:
    escolha = int(input('Escolha uma opção do menu:  '))
    if escolha == 1:
        soma = (n1 + n2)
        print('A soma de {} + {} = {}.'.format(n1, n2, soma))
    elif escolha == 2:
        multiplicar = (n1 * n2)
        print('A multiplicação de {} x {} = {}.'.format(n1, n2, multiplicar))
    elif escolha == 3:
        if n1 > n2:
            print('O número {} > {}.'.format(n1, n2))
        else:
            print('O número {} > {}.'.format(n2, n1))
    elif escolha == 4:
        n1 = int(input('Escolha um número:   '))
        n2 = int(input('Escolha um número:   '))
        print('Seus novos números são {} e {}.'.format(n1, n2))
print('Tchau! Até a próxima')
print('Obrigada!')

