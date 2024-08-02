def cab(a):
    print('-' * 30)
    print(f'{a:^30}')
    print(f'-' * 30)


def fatorial(b, show=False):
    from math import factorial
    """
    Cálculo Fatorial
    - b: o número que deseja ser calculado
    - show: deseja mostrar o cálulo (True) ou apenas resultado final (false)
    """
    if show == True:
        for f in range(b, 0, -1):
            print(f'{f}', end='')
            if f > 1:
                print(' x ', end='')
        print(f' = {factorial(b)}')
    else:
        n = (factorial(b))
        print(n)

    print('-' * 30)


cab('CÁLCULO FATORIAL')
fatorial(5)
