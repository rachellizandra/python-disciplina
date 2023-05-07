# Implementar uma solução que retorne o menor elemento de uma lista

def retornarMenorElemento(array):
    menor = lista[0] 
    for elem in array:
        if(elem < menor):
            menor = elem
    return menor

lista = [10, 2, 5, 7, 6, 3]
menor_numero = retornarMenorElemento(lista)
print(menor_numero)

