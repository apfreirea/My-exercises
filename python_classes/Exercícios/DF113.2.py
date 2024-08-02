def leiaInt():
    try:
        n = int(input('Digite um número:  '))
    except ValueError:
        print(f'O valor digitado não é um número inteiro. ')
        n = str(input('Digite um número:  '))
    else:
        print(f'Você digitou o número {n}.')



leiaInt()


def leiaFloat():
    try:
        num = float(input('Digite um número:  '))
    except ValueError:
        print('O valor digitado não é um número!')
        num = float(input('Digite um número:  '))
    else:
        print(f'Você digitou {num:.2f}.')



leiaFloat()