
nomes=[]
idades=[]
sexos=[]

for dados in range(2):
    nome=str(input('Qual o seu nome?   '))
    idade=int(input('Qual a sua idade?   '))
    sexo=str(input('Sexo f ou m?   ')).upper()
    nomes.append(nome)
    idades.append(idade)
    sexos.append(sexo)
print('Os nomes dos participantes da pesquisa são: {}.'.format(nomes))
print('As idades dos participantes da pesquisa são: {}.'.format(idades))
print('O sexo dos participantes da pesquisa são: {}.'.format(sexos))
soma=sum(idades)
medi=soma/len(idades)
print('A média de idade dos participantes é: {}.'.format(medi))

# Achar homem mais velho
velho=-1
nome_velho='' # string vazia

for i in range(len(nomes)):
    if sexos[i] == 'M' and idades[i] > velho:
        velho = idades[i]
        nome_velho = nomes[i]
if nome_velho:
        print('O homem mais velho é {} com {} anos.'.format(nome_velho,velho))
else:
        print('Homens não foram listados.')

# Achar mulheres maiores de 20 anos

mulher=0
for i in range(len(nomes)):
    if sexo == 'F' and idade > 20:
        mulher += 1
    else:
        print('Não há mulheres maiores de 20 anos.')
print('Existem {} mulheres maiores de 20 anos.'.format(mulher))
