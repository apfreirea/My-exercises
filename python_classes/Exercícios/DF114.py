# Teste do pudim

import webbrowser

# Site
try:
    url = str(input('Digite a url: '))
    webbrowser.open(url)
except:
    print('Não foi possível abrir o site no momento!')
else:
    print('Site acessado com sucesso!')
