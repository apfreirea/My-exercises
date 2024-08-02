from time import sleep
def contador(i,f,p):

    r = str(input('Deseja fzr contagem decrescente? S/N')).upper()
    if r == 'S':
        i = int(input('Valor de início:  '))
        f = int(input('Valor do fim:  '))
        p = int(input('Passo:')) * (-1)
        for c in range(f, i, p):
            print(f'{c}', end=' ')
            sleep(0.5)
    elif r =='N':
        i = int(input('Valor de início:  '))
        f = int(input('Valor do fim:  '))
        p = int(input('Passo:'))
        for c in range(i, f, p):
            print(f'{c}', end=' ')
            sleep(0.5)


contador(0,20,1)