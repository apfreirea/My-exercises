import math as m
cto=float(input('Informe o valor do cateto oposto: '))
cta=float(input('Informe o valor do cateto adjacente:  '))
print('Vamos calular a hipotenusa, ok?!')
h=m.sqrt((m.pow(cto,2)) + (m.pow(cta,2)))
print('O valor  da hipotenusa de acordo com os números fornecidos é {:.2f}!'.format(h))