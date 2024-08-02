n = int(input('Quantos termos da sequência de Fibonacci deseja?'))

print('  --'*12)
t0=0
t1=1
t2=0
cont=3
print('{}  {}  '.format(t0,t1),end='')
while cont <= n:
    t2=t1+t0
    cont += 1
    print('{}  '.format(t2),end='')
    t0=t1
    t1=t2
    t2=t0+t1
print('fim')