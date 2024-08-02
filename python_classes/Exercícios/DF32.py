ano=float(input('Qual ano você está?    '))
if ano % 4 == 0 and ano % 400 == 0 or ano % 100 == 0:
    print('o ano de {} é bissexto!'.format(ano))
else:
    print('O ano de {} não é bissexto!'.format(ano))
print('fim')