
dist=float(input('Qual a distância em km até o destino desejado?    '))
if dist <= 200:
    print('O preço da sua passagem é {:.2f} reais.'.format(dist*0.5))
else:
    print('O preço da sua passagem será {:.2f} reais.'.format(dist*0.45))
print('fim')