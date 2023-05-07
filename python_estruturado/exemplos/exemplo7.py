# Implementar uma solução que some todos os numeros pares de uma lista
# exemplo: lista = [10, 2, 5, 7, 6, 3] o somatorio é 18

lista = [10, 2, 5, 7, 6, 3]
n = len(lista)
soma = 0
for i in range(n):
    if(lista[i] % 2 == 0):
        soma += lista[i]
print(f'O somatório dos elementos pares da lista é {soma}')

#ou 

lista = [10, 2, 5, 7, 6, 3]
soma = 0
for num in lista:
    if(num % 2 == 0):
        soma += num
print(f'O somatório dos elementos pares da lista é {soma}')