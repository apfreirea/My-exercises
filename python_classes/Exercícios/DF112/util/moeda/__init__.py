def aumentar(v, pa, sit=False):
    """
    FUNÇÃO AUMENTAR
    Parâmetro p: número da qual se deseja cálcular o aumento
    Parâmetro aum: cálculo de aumento de 30% sobre p.
    """
    aum = v + v * (pa / 100)
    if sit == True:
        return print(f'R${(aum):.2f}')
    else:
        return print(f'Um aumento de {pa}% em R${v:.2f} = R${(aum):.2f}')


def metade(v, sit=False):
    met = v / 2
    if sit == True:
        return print(f'R${(met):.2f}')
    else:
        return print(f' A metade de R${v:.2f} = R${(met):.2f}')


def dobro(v, sit=False):
    dob = v * 2
    if sit == True:
        return print(f'R${(dob):.2f}')
    else:
        return print(f' O dobro de R${v:.2f} = R${dob:.2f}')


def reduzir(v, pr, sit=False):
    redu = v - v * (pr / 100)
    if sit == True:
        return print(f'R${(redu):.2f}')
    else:
        return print(f'Uma redução de {pr}% e R${v:.2f} = R${(redu):.2f} ')


def resumo(v=0, pa=10, pr=10):
    if v is float:
        redu = v - v * (pr / 100)
        dob = v * 2
        met = v / 2
        aum = v + v * (pa / 100)
        print('-' * 50)
        print('RESUMO DOS VALORES'.center(50))
        print('-' * 50)
        print()
        print(f'Preço analisado: \tR${(v):.2f}')
        print(f'Dobro do preço: \tR${(dob):.2f}')
        print(f'Metade do preço: \tR${(met):.2f}')
        print(f'{pa}% de aumento: \tR${(aum):.2f}')
        print(f'{pr}% de redução: \tR${(redu):.2f}')
        print('-' * 50)
