n = soma = 0
cont = 0
while True:
    n = int(input('Digite um valor:   '))
    print('Para parar o programa digite 99.')
    if n == 99:
        break
    soma += n
    cont += 1
print(f'Você digitou {cont} números. A soma entre eles é {soma}.')