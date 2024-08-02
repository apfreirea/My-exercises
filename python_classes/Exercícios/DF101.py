def voto():
    from datetime import date
    d = date.today().year
    print('-' * 30)
    print(f'{"SITUAÇÃO DE VOTO":^30}')
    print('-' * 30)
    ano = int(input('Qual seu ano de nascimento? '))
    idade = d - ano
    if idade < 16:
        print(f'Você tem apenas {idade} anos.\n {"Voto NEGADO!":^30}')
    elif 16 <= idade < 18 or idade >= 70:
        print(f'Você tem {idade} anos.\n {"Voto OPCIONAL!":^30}')
    elif 18 <= idade < 70:
        print(f'Você possui {idade} anos. \n {"Voto OBRIGATÓRIO!":^30}')
    print()
    print(f'{"Até a próxima!":^30}')
    print('-' * 30)


voto()