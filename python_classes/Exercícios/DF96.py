def cab(msg):
    print('-'*36)
    print(msg)
    print('-'*36)




def area(c, larg):
    larg = float(input('LARGURA:  '))
    c = float(input('COMPRIMENTO:  '))
    a = c * larg
    print(f'A área do terreno de {larg}x{c} é {a} m².')


cab('ÁREA DO TERRENO')
area(50, 25)
