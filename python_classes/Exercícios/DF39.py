ano=int(input('Qual seu ano de nascimento?   '))
alist=2024-ano
falt=18-alist
past=alist-18
if alist < 18:
    print('Com apenas {} anos, você ainda é jovem. Faltam {} anos para se alistar.'.format(alist,falt))
elif alist == 18:
    print('Você possui {} anos. Está na hora de fazer seu alistamento.'.format(alist))
elif alist > 18:
    print('Você já está com {} anos. Seu período de alistamento passou há {} anos atrás.'.format(alist,past))