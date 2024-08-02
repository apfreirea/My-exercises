n1 = float(input('Digite sua primeira nota:  '))
n2 = float(input('Digite sua segunda nota:   '))
media=(n1+n2)/2
print('Sua média foi {:.2f}.'.format(media))
if media <= 5.99:
    print('Infelizmente você foi reprovado!')
else:
    if media <= 6.99:
        print('Você está de recuperação!')
    else:
            print('Parabéns! Você está aprovado!')
print('-fim-')