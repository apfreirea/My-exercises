def leiadinheiro():
    from termcolor import colored

    n = str(input('Digite um valor: '))
    while n.isalpha() or n == '':
        print(colored(f'ERRO: {n} não é válido!', 'red'))
        n = str(input('Digite um valor: '))
    val = n.replace(',', '.')
    v = float(val)
    return v
