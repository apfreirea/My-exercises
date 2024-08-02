um=0
dois=0
lt1=[]
lt2=[]
asw=''

while asw != 'N':
    um = int(input('Digite um número:  '))
    dois = int(input('Digite um número:  '))
    print('Os números escolhidos são {} e {}.'.format(um,dois))
    lt2.append(um)
    lt1.append(dois)
    if um > dois:
        print('Onde {} > {}.'.format(um,dois))
    else:
        print('Onde {} > {}.'.format(dois,um))
    media=(um+dois)/2
    print('E a média entre eles é {}.'.format(media))
    asw=str(input('Deseja digitar novos números? Sim/Não')).upper()[0]
print('Até mais!')