import math as m
r1=int(input('Digite o valor da reta 1:   '))
r2=int(input('Digite o valor da reta 2:   '))
r3=int(input('Digite o valor da reta 3:   '))
if (r1+r2) <= r3:
    print('As retas formam um triângulo.')
else:
    if (r1+r3) <= r2:
        print('Essas retas não formam um triângulo')
    else:
        if (r2+r3) <= r1:
            print('Essas retas formam um triângulo')
        else:
            print('Essas retas não formam um triângulo.')
print('fim ')