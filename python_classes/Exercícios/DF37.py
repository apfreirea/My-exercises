
num=int(input('Digite um número inteiro:   '))
print('''Escolha o número da base que deseja converte: 
[1] binário 
[2] octal 
[3] hexadecimal''')
base=int(input('Sua opção é    '))
if base ==1:
    print('{} convertido para binário é {}.'.format(num,bin(num)))
elif base ==2:
    print('{} convertido para octal é {}.'.format(num,oct(num)))
elif base ==3:
    print('{} convertido para hexagonal é {}.'.format(num,hex(num)))
else:
    print('Opção inválida!')