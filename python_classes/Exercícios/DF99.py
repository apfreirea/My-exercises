def cab(msg):
    print('-'*36)
    print(msg)
    print('-'*36)


cab('ANÁLISE DE NÚMERO MAIOR')

maior = []

print()
r = input('Deseja adicionar um número? S/N ').upper()
while True:
    if r == 'S':
        mais = int(input('NÚMERO: '))
        if not maior or mais > maior[-1]:
            maior.append(mais)
        else:
            posicao = 0
            while posicao < len(maior):
                if mais <= maior[posicao]:
                    maior.insert(posicao, mais)
                    break
                posicao += 1
        r = str(input('Desja adicionar um número? S/N')).upper()
    elif r == 'N':
        break
    print()

print(maior)