print('- -- - NOTAS ESCOLARES - -- -')

pessoa = []
dados = []
r = str(input('\nDeseja cadastrar alguém? S/N')).upper()

while True:
    if r == 'S':
        nome=str(input('Nome:  '))
        n1=float(input('Nota 1:  '))
        n2=float(input('Nota 2:  '))
        med=(n1+n2)/2
        dados.append(nome)
        dados.append(n1)
        dados.append(n2)
        dados.append(med)
        pessoa.append(dados[:])
        dados.clear()
        r = str(input('Deseja cadastrar alguém? S/N')).upper()
    else:
        break

for a in pessoa:
    print(f'\n{"Aluno":<10}{"Nota 1":^10}{"Nota 2":^10}{"Média":^10}')
    print(f'{a[0]:<10}{a[1]:^10.2f}{a[2]:^10.2f}{a[3]:^10.2f}')