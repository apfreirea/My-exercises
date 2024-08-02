import math as m
peso = float(input('Qual o seu peso?   '))
altura = float(input('Qual a sua altura em metros?   '))

imc = peso/(m.pow(altura,2))

if imc <= 18.5:
    print('Seu IMC é {:.2f}. Você está abaixo do seu peso.'.format(imc))
elif imc <= 25:
    print('Seu IMC é {:.2f}. Você está no seu peso ideal.'.format(imc))
elif imc <= 30:
    print('Seu IMC é {:.2f}. Você está com sobrepeso.'.format(imc))
elif imc <= 40:
    print('Seu IMC é {:.2f}. Esse caso é considerado obesidade.'.format(imc))
elif imc > 40:
    print('Seu IMC é {:.2f}. Esse caso é considerado obesidade mórbida.'.format(imc))