valor=float(input('Qual o valor do imovél que deseja comprar?     '))
salario=float(input('Qual seu salário atual?     '))
ano=int(input('Em quantos anos pretende pagar seu emprestimo?    '))

prest= (valor/(12*ano))
if prest <= (salario*(30/100)):
    print('Sua parcela será de {:.2f} reais ao mês ao longo de {} anos.'.format(prest,ano))
elif prest > (salario*(30/100)):
    print('A parcela de {:.2f} reais, excedeu 30% do seu salário.'.format(prest))
    print('Infelizmente seu emprestimo foi negado!')