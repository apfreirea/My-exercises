n1=float(input('Qual a altura da sua parede em metros?'))
n2=float(input('Qual a largura da sua parede em metros?'))
area=n1*n2
tinta=(area/2)
print('A área da sua parede é {:.2f} m^2, logo será necessário {:.2f} litros de tinta para pintá-la.'.format(area,tinta))
