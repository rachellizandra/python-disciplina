# Implementar uma solução que faça o tratamento de exceção de divisão por zero.

def dividir(x, y):
    try:
        resultado = x / y
        print(f'A resposta é {resultado}')
    except ZeroDivisionError:
        print('Divisão por zero')

dividir(3, 0)
dividir(3, 1)