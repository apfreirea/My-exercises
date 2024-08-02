from datetime import date
print('---- DADOS PESSOAIS ----')
print()

biblioteca = []
dados={}
r = str(input('Deseja cadastrar seus dados? S/N')).upper()
while True:
    if r == 'S':
        dados['Nome']=str(input('Digite seu nome:  '))
        dados['Ano']=int(input('Ano de nascimento:  '))
        dados['Sexo']=str(input('Sexo: ')).upper()[0]
        dados['Idade']=(date.today().year)-(dados['Ano'])
        dados['CTPS']=int(input('CTPS:  '))
        biblioteca.append(dados.copy())
        if dados['CTPS'] != 0:
            dados['Contratação']=int(input('Qual ano foi contratado(a)? '))
            dados['Salário']=float(input('Qual seu salário?  '))
            biblioteca.append(dados.copy())
        if dados['Sexo'] == 'F':
            dados['Aposentadoria']=62
            biblioteca.append(dados.copy())
        elif dados['Sexo'] == 'M':
            dados['Aposentadoria']=65
            biblioteca.append(dados.copy())
        dados['Tempo']=((dados['Contratação'])+30)-(dados['Ano'])
        biblioteca.append(dados.copy())
        r = str(input('Deseja cadastrar novos dados? S/N')).upper()
    else:
        break
print()
print('---- Aposentadoria ----')

print(f'Por tempo de serviço você se aposentaria com ',end='')
print(dados['Tempo'],end=' ')
print('anos.')
print(f'Porém, para se aposentar por idade você se aposenta com ',end='')
print(dados['Aposentadoria'],end=' ')
print('anos.')

print('Até mais!')
print('--'*12)
