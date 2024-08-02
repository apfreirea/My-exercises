def cab(a):
    print('-' * 30)
    print(f'{a:^30}')
    print(f'-' * 30)


cab('CADASTRO DE ALUNOS')
r = str(input('Cadastrar alunos? S/N')).upper()

geral = []
alunos = {}
nota = 0
while True:
    if r == 'S':
        # alunos.clear()
        alunos['Nome'] = str(input('Aluno: '))
        alunos['Notaum'] = float(input('Digite Nota 1: '))
        nota += 1
        alunos['Notadois'] = float(input('Digite Nota 2: '))
        nota += 1
        alunos['Média'] = (alunos['Notaum'] + alunos['Notadois']) / 2
        if alunos['Média'] >= 7:
            alunos['Situação'] = 'APR'
        elif 5 <= alunos['Média'] < 7:
            alunos['Situção'] = 'RC'
        elif alunos['Média'] < 5:
            alunos['Situação'] = 'REP'
        geral.append(alunos.copy())
        r = str(input('Cadastrar novo aluno? S/N')).upper()
    else:
        break
print()
cab('SITUAÇÃO DA TURMA')
print(f" {'ALUNO':^5} {'NOTA 1':^12} {'NOTA 2':^16} {'MÉDIA':^20} {'SITUAÇÃO':^25}  ")
for i in geral:
    print(f"{i['Nome']:^5}{i['Notaum']:^14}{i['Notadois']:^18}{i['Média']:^22}{i['Situação']:^28}  ")

cab('BALANÇO')

if nota == 0:
    print(f'Nenhuma nota foi cadastrada!')
elif nota == 1:
    print(f'Uma nota foi cadastrada!')
elif nota > 1:
    print(f'Foram cadastradas {nota} notas.')
print()

for i in geral:
    if i['Notaum'] > i['Notadois']:
        maior = i['Notaum']
    else:
        maior = i['Notadois']
print(maior)