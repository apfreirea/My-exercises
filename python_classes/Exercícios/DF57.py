sexo=str(input('Digite seu sexo: F ou M.')).strip().upper()[0] # o zero serve pra dizer que vai pegar só a primeir letra
while sexo not in 'MmFf':
    print('hm, resposta insatisfatória.')
    sexo=str(input('Digite novamente seu sexo: F ou M.'))
print('Obrigada!')