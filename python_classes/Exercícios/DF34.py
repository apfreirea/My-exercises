sal=float(input('Qual o valor do seu salário atual?    '))
if sal <= 1250:
    print('Seu salário com reajuste de 15% irá para R$ \033[32m{:.2f}\033[m .'.format(sal+sal*(15/100)))
else:
    print('Seu salário com reajuste de 10% irá para R$ \033[32m{:.2f}\033[m.'.format(sal+sal*(10/100)))
print('fim')  