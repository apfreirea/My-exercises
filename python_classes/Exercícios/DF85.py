print(' --- Escolha os números ---')
numero = [[], []]
for n in range(0, 7):
    num = int(input('Digite um número:  '))
    if num % 2 == 0:
        numero[0].append(num)
    if num % 2 != 0:
        numero[1].append(num)

print(f'Os números escolhidos foram {numero}.')
print(f'Os números pares são {numero[0]}.')
print(f'Os números pares são {numero[1]}.')