n1=int(input('Escolha um número:   '))
n2=int(input('Escolha outro número:   '))

if n1 > n2:
    print('O número {} é maior que {}.'.format(n1,n2))
elif n1 < n2:
    print('O número {} é maior que {}.'.format(n2,n1))
elif n1 == n2:
    print('Os números {} e {} são iguais.'.format(n1,n2))
print('fim')
