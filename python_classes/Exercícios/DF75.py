cont = 0
n= (int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: ')),
     int(input('Digite um número: ')))
print(f'Número 9 apareceu {n.count(9)} vezes.')

for num in range(4):
    if n[num] % 2 == 0:
        cont += 1
print(f'\nForam digitados {cont} números pares.')

for num in range(4):
    if 3 in n:
        print(f'\nO valor 3 está na posição {n.index(3) + 1}°.')
        break
    else:
        print('Não foi digitado nenhum número 3.')
        break
