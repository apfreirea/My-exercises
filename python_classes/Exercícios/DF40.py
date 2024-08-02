n1=float(input('Qual sua primeira nota?   '))
n2=float(input('Qual sua segunda nota?    '))
med=(n1+n2)/2
rec=7-med
if med >= 7:
    print('Sua média é {}. Você está aprovado!'.format(med))
elif med >= 5:
    print('Sua média é {}, faltou {} pontos para ser aprovado. Você está de recuperação!'.format(med,rec))
else:
    print('Sua média é {}. Você está reprovado!'.format(med))
print('Até a próxima!')