
n1=float(input('Qual o seu salário?'))
print('Seu salário é R${}, correto?'.format(n1))
aum = n1 + (n1*(15/100))
print('Caso você receba 15% de aumento, seu novo salário será de R${}.'.format(aum))