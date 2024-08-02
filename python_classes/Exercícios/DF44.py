preco = float(input('Qual o preço do produto?     '))
pag = float(input('Escolha o número de acordo com sua opção de pagamento: \n 1. À vista - dinheiro ou cheque; \n 2. À vista - cartão; \n 3. 2x no cartão; \n 4. 3x ou mais no cartão. \n'))

if pag == 1:
    print('O produto custará {}.'.format(preco*(1-10/100)))
elif pag == 2:
    print('O produto custará {}.'.format(preco*(1-5/100)))
elif pag == 3:
    print('O produto custará {}.'.format(preco))
elif pag == 4:
    print('O produto custará {}.'.format(preco/(1 + 20/100)))
print('Boas compras!')