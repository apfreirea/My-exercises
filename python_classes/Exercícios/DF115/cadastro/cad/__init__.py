def cabeça():
    print('-' * 40)
    print(f'{"MENU":^40}')
    print('-' * 40)
    print()


def menu():
    while True:
        print('1 - Ver pessoas cadastradas ')
        print(f'2 - Cadastrar pessoas')
        print(f'3 - Sair do sistema')

        dados = []
        usuarios = {}
        try:
            op = int(input('Sua Opção:  '))
        except ValueError:
            print('Número inválido!')
        if op == 1:
            if dados:
                for c in dados:
                    print(usuarios)
                    print(f'O usuário {c["NOME"]} tem {c["IDADE"]}')
            else:
                print('Nenhum usuário cadastrado!')
        elif op == 2:
            usuarios['Nome'] = str(input('NOME:'))
            usuarios['IDADE'] = int(input('IDADE:'))
            dados.append(usuarios.copy())
            print('Usuário cadastrado!')
        elif op == 3:
            print('Obrigado! \nAté a próxima!')
            break
