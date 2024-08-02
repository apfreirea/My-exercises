s = 0
n=500
for numeros in range(1,n,2):
    if numeros % 3 == 0:
        s = s + numeros
print(' A soma de todos os multiplos de 3 entre 0 e 500 é {}'.format(s))
print('cabou')
