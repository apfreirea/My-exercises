a=int(input('Digite o termo geral:  '))
r=int(input('Digite a razão que desenha:   '))

dez=a+(10-1)*r # esse 10 se deve pois queremo o 10° termo
for pa in range(a,dez+r,r):
        print(pa)
print('acabou')