num=int(input('Escolha um número'))
div = 0
for primo in range(1,num+1):
    if num % primo == 0:
        div = div +1
if div == 2:
    print('É primo, pois é divisível apenas por 1 e por {}.'.format(num))
else:
    print('Não é primo pois entre 1 e {}, ele possui {} divisores.'.format(num,div))