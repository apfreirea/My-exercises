import random as r

na1 = str(input('Digite o nome do aluno 1: '))
na2 = str(input('Digite o nome do aluno 2: '))
na3 = str(input('Digite o nome do aluno 3: '))
na4 = str(input('Digite o nome do aluno 4: '))

lt=[na1,na2,na3,na4]
sqq=r.sample(lt,k=4)
print('A sequência de a presentação será: {}'.format(sqq))