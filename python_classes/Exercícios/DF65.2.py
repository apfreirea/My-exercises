ttl=[]
ask= 'S'
tamano = soma = media = maximo = minimo = 0
while ask == 'S':
    num=int(input('Escolha um número:   '))
    ttl.append(num)
    tamanho=len(ttl)
    soma=sum(ttl)
    media=soma/tamanho
    maximo=max(ttl)
    minimo=min(ttl)
    ask=str(input('Deseja escolher mais um número? S/N')).upper()
print('A média dos números escolhidos é {}.'.format(media))
print('O maior valor escolhido foi {} e o menor foi {}.'.format(maximo,minimo))
print('Até mais!')