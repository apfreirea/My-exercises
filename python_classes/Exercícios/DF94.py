print('---' * 15)
print(f'{"CADASTRO DE PESSOAS":^45}')
print('---' * 15)
cadastro = []
pessoa = {}
idades = 0
media = 0
cont = 0
som = 0
print()
r = str(input('Deseja cadastrar alguém? S/N')).upper()[0]
print()

while True:
    if r == 'S':
        pessoa['Nome'] = str(input('Digite seu nome:  '))
        cont += 1
        pessoa['Sexo'] = str(input('Qual seu sexo?')).upper()[0]
        pessoa['Idade'] = int(input('Qual a sua idade?  '))
        i = pessoa['Idade']
        print()
        idades += i
        media = idades / cont
        cadastro.append(pessoa.copy())
        r = str(input('Deseja cadastrar mais alguém? S/N')).upper()[0]
    elif r == 'N':
        break
print()
print('---' * 15)
print(f'{"ANÁLISE DOS DADOS":^45}')
print('---' * 15)
print(f'Número de pessoas cadastradas: {cont} pessoas.')
print(f'Média de idade das pessoas cadastradas: {media} anos.')

print(f'\nLista de mulheres cadastradas:\n', end='')
for i in cadastro:
    if i['Sexo'] == 'F':
        print(i['Nome'])
print(f'\nLista de pessoas acima da média de idade: \n')
for j in cadastro:
    if j['Idade'] > media:
        print(j['Nome'])


