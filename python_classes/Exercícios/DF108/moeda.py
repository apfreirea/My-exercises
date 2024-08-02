def aumentar(v, p):
    """
    FUNÇÃO AUMENTAR
    Parâmetro p: número da qual se deseja cálcular o aumento
    Parâmetro aum: cálculo de aumento de 30% sobre p.
    """
    return print(f'Um aumento de {p}% em R${v:.2f} = R${v + v * (p / 100):.2f}')


def metade(p):
    return print(f' A metade de R${p:.2f} = R${p / 2:.2f}')


def dobro(p):
    return print(f' O dobro de R${p:.2f} = R${p * 2:.2f}')


def reduzir(v, p):
    return print(f'Uma redução de {p}% e R${v:.2f} = R${v - v * (p / 100):.2f} ')
