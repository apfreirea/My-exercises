lista=[]
nums = int(input('Digite um número ou 999 para parar:   '))
cont = 0
while nums != 999:
    if nums != 999:
        lista.append(nums)
        nums=int(input('Digite um número ou 999 para parar:  '))
        soma=sum(lista)
        tamanho=len(lista)
print(lista)
print('Você digitou {} números e a soma deles é {}.'.format(tamanho,soma))
