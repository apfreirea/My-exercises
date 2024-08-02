
import math as m
r1=int(input('Digite o valor da reta 1:   '))
r2=int(input('Digite o valor da reta 2:   '))
r3=int(input('Digite o valor da reta 3:   '))

if (r2 + r3) < r1 or (r1 + r3) < r2 or (r1 + r2) < r3:
    print('As retas formam um triângulo.')
    if  (r1 == r2 and r2 == r3):
        print('Esse triângulo é equilátero.')
    elif (r1 ==r2 or r1 == r3 or r2 == r3):
        print('Esse triângulo é isósceles.')
    else:
        print('Esse triângulo é escaleno')
else:
    print('Essas retas não formam um triângulo')