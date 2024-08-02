n=4

from datetime import date
atual = date.today().year



save=0
for idade in range(1,n+1,1):
    nasc=int(input('Qual seu ano de nascimento? \n'))
    id = atual - nasc
    if id > 18:
        save += 1
print('{} pessoas já atingiram a maior idade.'.format(save))