
pesos=[]

for pessoas in range (5):
    peso=int(input('Qual o seu peso?\n'))
    pesos.append(peso)
pesos.sort()
print('Os pesos informados foram: {}'.format(pesos))

# "pessoas" é o meu contado que vai interagir 5 vezes
# "input" captura o valor digitado e armazena na variavel "peso"
# o "f" é usado para contar de 1 a 5 qual o peso que ele tá digitando
# a função append() pega os nomes digitados na variavel 'peso' e adiciona em uma lista chamada 'pesos' \n
## que foi declarada em branco aterriormente.
## é importante dentro do parentesis do append() informar qual a variavem que tá recebendo os valores que vão virar lista. Nesse caso 'peso'
