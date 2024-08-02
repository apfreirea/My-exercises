print('Gerador de Progressão Aritmética')
print('--'*16)

a=int(input('Digite o termo geral:  '))
r=int(input('Digite a razão que desenha:   '))

# começar a contagem

termo = a
cont = 1

while cont <=10:
    print('{} -'.format(termo), end='')
    termo += r
    cont += 1
print(termo)