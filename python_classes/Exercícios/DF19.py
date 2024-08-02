from random import choice

na1 = str(input('Digite o nome do aluno 1: '))
na2 = str(input('Digite o nome do aluno 2: '))
na3 = str(input('Digite o nome do aluno 3: '))
na4 = str(input('Digite o nome do aluno 4: '))
lt = [na1, na2, na3, na4]
esc = choice(lt)
print('O aluno escolhido foi {}'.format(esc))