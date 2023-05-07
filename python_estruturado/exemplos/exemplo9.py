# Implementar solução que retorne a soma de todos os elementos pares de uma lista

def retornarSomaPares(array):
    soma = 0
    for elem in array:
        if(elem % 2 == 0):
            soma += elem
    return soma

lista = [10, 2, 5, 7, 6, 3]
soma = retornarSomaPares(lista)
print(f'O somatório dos elementos pares desta lista é: {soma}')