
dias=int(input('Qual a quantidade de dias que deseja alugar o carro?'))
km=float(input('Quantos km pretende percorrer?'))
print('Você deseja alugar o carro por {} dias e percorrer {} km, certo? '.format(dias,km))
custo=((dias*60) + (km*0.15))
print('O valor total do aluguel será de R${:.2f}.'.format(custo))