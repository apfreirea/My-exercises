escolha=int(input('1.Pedra; 2.papel; ou 3.tesoura? \n'))
if escolha == 1 :
    print('Se você escolhe {}, eu escolho papel.'.format(escolha))
elif escolha == 2:
    print('Se você escolhe {}, eu escolho tesoura.'.format(escolha))
elif escolha == 3:
    print('Se você escolheu {}, eu escolho pedra.'.format(escolha))