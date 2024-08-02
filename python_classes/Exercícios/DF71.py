import math as m

print('BANCO CHARM')
troco = ''
saque = int(input('Qual valor deseja sacar?'))

while True:
    if saque > 0:
        cinq = m.trunc(saque / 50)
        if cinq > 0:
            print(f'Você receberá {cinq:.0f} notas de R$50,00.')
            troco = saque - (cinq * 50)

        if troco > 0:
            vinte = m.trunc(troco / 20)
            print(f'Você receberá {vinte:.0f} notas de R$20,00.')
            troco = troco - (vinte * 20)

        if troco > 0:
            dez = m.trunc(troco / 10)
            print(f'Você receberá {dez:.0f} notas de R$10,00.')
            troco = troco - (dez * 10)

        if troco > 0:
            um = m.trunc(troco / 1)
            print(f'Você receberá {um:.0f} notas de R$1,00.')
            troco = troco - (um * 1)
        if troco == 0:
            break
print('Tenha um bom dia!')