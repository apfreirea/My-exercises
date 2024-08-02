vel=float(input('Qual a velocidade do carro em km/h?   '))
mult=(vel-80)*7
if vel >= 80:
    print('Você foi multado em {:.2f} reais'.format(mult))
else:
    print('Parabéns por se manter no limite de velocidade!')
print('fim')