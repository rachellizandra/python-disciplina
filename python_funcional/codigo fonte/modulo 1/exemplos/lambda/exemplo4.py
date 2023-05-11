# Considere a lista =  [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
# Implementar uma solução através de programação funcional para imprimir apenas os números pares

lista =  [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

fTesteParidade = lambda x: x % 2 == 0

print(f'teste de paridade(5) = {fTesteParidade(5)}')

pares = list(filter(fTesteParidade, lista))

print(f'lista de números pares = {pares}')
