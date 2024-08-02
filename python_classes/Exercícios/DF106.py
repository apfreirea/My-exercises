def programas(n):
    from termcolor import colored
    print(colored('-' * 50, 'blue'))
    print(colored(f'{"SISTEMA DE AJUDA PYHELP":^50}', 'blue', 'on_grey'))
    print(colored('-' * 50, 'blue'))
    r = str(input('Deseja pesquisar uma biblioteca? S/N')).upper()
    while True:

        if r == 'S':
            n = str(input('Qual biblioteca deseja compreender?  '))
            help(n)

            print(colored('=' * 50, 'blue', 'on_grey'))
            r = str(input('Deseja pesquisar mais? S/N')).upper()
        else:
            print(colored('Até mais!', 'red', 'on_white'))
            break


programas(print)


