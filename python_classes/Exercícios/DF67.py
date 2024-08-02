num=int(input('De qual número deseja obter a tabuada?'))
print(f'O número escolhido foi {num}, certo?')
tab=''
while True:
    if num < 0:
        break
    for tab in range(0,10+1,1):
        print(f'{tab} x {num} = {tab*num}')
    print('Deseja obter a tabuada de outro número?')
    asw=str(input('Sim ou Não')).upper()
    if asw == 'SIM':
        num=int(input('De qual número deseja obter a tabuada?'))
    else:
        print('Até logo!')
print('tchau')