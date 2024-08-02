
valores=[]
par=[]
impar=[]
r = str(input('Deseja adicionar um número? S/N')).upper()
while True:
        if r == 'S':
            num=int(input('\nDigite um número:   '))
            valores.append(num)
        if num % 2 == 0:
            par.append(num)
            r = str(input('Deseja adicionar outro número? S/N')).upper()
        else:
            impar.append(num)
            r = str(input('Deseja adicionar outro número? S/N')).upper()
        if r == 'N':
            break
print(f'Os números adicionados foram {valores}.')
print(f'Os números pares digitados foram {par}')
print(f'Os números ímpares digitados foram {impar}')