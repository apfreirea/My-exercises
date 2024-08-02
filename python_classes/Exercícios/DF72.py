while True:
    nomes = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco')
    num = int(input('Digite um número entre 0 e 5:   '))
    if num < 0 or num > 5:
        print('Número inválido!')
        break
    else:
        print(f'Número: {nomes[num]}.')

print('Até a próxima!')