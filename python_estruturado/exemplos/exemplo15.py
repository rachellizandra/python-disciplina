# Implementar uma solução que faça o tratamento de exceção para verificar se a entrada é, de fato, um número.

try: 
    x = int(input('Digite um número:'))
except ValueError:
    print('Entre com um número válido.')