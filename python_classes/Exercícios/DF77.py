word = ('AMEIXA', 'AMEBA', 'CENOURA', 'CEBOLA', 'JUJUBA')

for w in word:
    print(f'\nPalavra {w} temos ', end='')
    for letra in w:
        if letra in 'AEIOU':
            print(letra, end='')
