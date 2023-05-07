# Implementar solução que retorne o fatorial de um numero

def fatorial(n):
    if(n == 0 or n == 1):
        return 1
    else:
        return n*fatorial(n-1)
    
numero = eval(input('Digite um número:'))
fatorial_numero = fatorial(numero)
print(f'O fatorial de {numero} é {fatorial_numero}')
