# from cadastro import cad
# cad.cabeça()
# cad.menu()

from cadastro.pessoas import *

pss = 'cursoemvideo.txt'

if not pessoasExist(pss):
    criarArquivo(pss)
    print('Arquivo encontrado')
else:
    print('Arquivo não existe!')

lerArquivo(cursoemvideo.txt)