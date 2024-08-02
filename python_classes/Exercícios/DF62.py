print('Gerador de Progressão Aritmética')
print('--'*16)

a=int(input('Digite o termo geral:  '))
r=int(input('Digite a razão que desenha:   '))

# começar a contagem

termo = a
cont = 1

while cont <=5:
    print('{} -'.format(termo), end='')
    termo += r
    cont += 1
print(termo)
# adicionar termos
contagem=cont
adicionais=termo
mais=int(input('Quantos termos mais quer mostar?'))
sm = contagem + mais

if mais != 0:
    while contagem <= sm:
        termo += r
        adicionais +=1
    print(adicionais)
    mais=int(input('Quer mais termos?'))
print('fim')

