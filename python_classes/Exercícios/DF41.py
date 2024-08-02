ano=int(input('Digite seu ano de nascimento:   '))
idade=2024-ano
if idade <= 9:
    print('Você tem {} anos. Você é um atleta MIRIM.'.format(idade))
elif idade <= 14:
    print('Você tem {} anos. Você é um atleta INFANTIL.'.format(idade))
elif idade <= 19:
    print('Você tem {} anos. Você é um atleta JUNIOR.'.format(idade))
elif idade <= 20:
    print('Você tem {} anos. Você é um atleta SÊNIOR.'.format(idade))
else:
    print('Você possui {} anos. Você é um atleta MASTER'.format(idade))
print('Bom campeonato!')