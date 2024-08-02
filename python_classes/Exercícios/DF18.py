import math as m
ang=float(input('Digite o valor do ângulo:  '))
s=m.sin(ang)
c=m.cos(ang)
tg=m.tan(ang)
print('Para o ângulo de {}°, o seno é {:.4f}, o cosseno é {:.4f} e a tangente é {:.4f}.'.format(ang,s,c,tg))