pilha = []

exp = str(input('Digite uma expressão:  '))

for simb in exp:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break

if len(pilha) == 0:
    print('Essa expressão é válida!')
else:
    print('Expressão inválida!')
