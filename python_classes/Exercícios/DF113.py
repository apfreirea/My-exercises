try:
    a = int(input('Número: '))
    b = int(input('Número: '))
    r = a/b
except (ValueError, TypeError):
    print('Tivemos um problema com os dados que você digitou!')
except ZeroDivisionError:
    print('Não é possível dividir por zero!')
except KeyboardInterrupt:
    print('O usuário não digitou um valor!')
except Exception as erro:
    print(f'O erro encontrado foi {erro.__class__}')
else:
    print(f'Resultado: {r:.2f}')
finally:
    print('Volte sempre!')