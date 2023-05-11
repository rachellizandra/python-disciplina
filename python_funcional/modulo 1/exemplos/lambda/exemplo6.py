# Considere a lista abaixo: 

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Implementar uma solução através de programação funcional para somar todos os elementos da lista

from functools import reduce

f_somar = lambda x, y: x + y

resultado = reduce(f_somar, numeros)

print(resultado)