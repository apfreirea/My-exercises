aluno = {'Nome':'Ana','Média':9.5}

for k,v in aluno.items():
    print(f'A Aluna {aluno["Nome"]} tem média {aluno["Média"]}\n')
if aluno['Média'] > 7:
    aluno['Situação']='Aprovada!'
    print(aluno['Situação'])
    print(aluno)