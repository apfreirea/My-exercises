times=('Flamengo','Bahia','Botafogo','Palmeiras','Cruzeiro','Athletico-PR','São Paulo','Bragantino','Internacional','Atlético-MG','Fortaleza','Juventude','Criciúma','Cuiabá','EC Vitória','Vaxco da Gama','Atlético-GO','Corinthians','Grêmio','Fluminense')

print(f'Os cinco primeiros colocados são: {times[0:5]}. \n')

print(f'Os quatro últimos colocados são: {times[16:20]}. \n')

print('Os times ocupantes das 20 posiõçes do Campeonato Brasileiro em ordem alfabética são: \n ')
print(sorted(times))
print('\n')
print(f'A posição do Palmeiras na tabela é: ', end='')
print(times.index('Palmeiras'))