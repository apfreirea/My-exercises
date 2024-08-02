def leiaInt():
    n = str(input('Digite um número:  '))
    while True:
        if n.isnumeric():
            n = int(n)
            print(f'Você digitou o número {n}.')
            break
        else:
            print('Digite um número válido!')
            n = str(input('Digite um número:  '))


leiaInt()