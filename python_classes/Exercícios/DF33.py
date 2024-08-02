n1=int(input('Digite um número.'))
n2=int(input('Digite outro número diferente do anterior.'))
n3=int(input('Digite um número diferente dos anteriores'))

if (n1>n2) and (n2>=n3):
    print('A ordem crescente dos números é {}, {} e {}.'.format(n3,n2,n1))
else:
    if (n1>n3) and (n3>=n2):
        print('A ordem crescente dos números é {}, {} e {}.'.format(n2,n3,n1))
    else:
        if (n2>n1) and (n1>=n3):
            print('A ordem crescente dos números é {}, {} e {}.'.format(n3,n1,n2))
        else:
            if (n2>n3)and(n3>=n1):
                print('A ordem crescente dos números é {}, {} e {}.'.format(n1,n3,n2))
            else:
                if (n3>n1) and (n1>=n2) :
                    print('A ordem crescente dos números é {}, {} e {}.'.format(n2,n1,n3))
                else:
                    print('A ordem crescente dos números é {}, {} e {}.'.format(n1,n2,n3))
print('fim')