cont = 0
man = 0
woman = 0

while True:

    idade = int(input('Qual a sua idade?   '))
    sexo = str(input('Seu sexo é feminino(f) ou masculino(m) ? ')).upper()[0]
    if idade >= 18:
        cont += 1

    if sexo == 'M':
        man += 1
        print(f'Você possui {idade} anos e é do sexo {sexo}, certo?!')
        ask = str(input('Deseja continuar? S/N')).upper()[0]

    elif sexo == 'F':
        woman += 1
        print(f'Você possui {idade} anos e é do sexo {sexo}, certo?!')
        ask = str(input('Deseja continuar? S/N')).upper()[0]

    elif sexo != 'MF':
        print('Resposta inválida!')
        ask = str(input('Deseja continuar? S/N')).upper()[0]

    if ask == 'N':
        break

print(
    f' Foram cadastradas {cont} pessoas maiores de 18 anos. \n Foram cadastrados {man} homens. \n Foram cadastradas {woman} maiores de 20 anos.')

print('Até mais!')