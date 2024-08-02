
frase=str(input('Digite sua palavra: \n')).strip().upper() #para remover espaços
palavras=frase.split()  # para quebrar em palavras
juntar=''.join(palavras) # para juntar as letras
inverter=''
for palindromo in range(len(juntar)-1,-1,-1):
  #  print(juntar[palindromo])
    print(juntar[palindromo], end='')
    inverter += juntar[palindromo]
if inverter == juntar:
    print(' \n \n é palindromo')
else:
    print('\n \n não é palindromo')


# len(junto) -1 == se tem 20 letras precisa pegar do 0 ao 19
# -1 vai até a letra -1 pois a primeira letra é 0
# -1 pra ir voltando as letras
