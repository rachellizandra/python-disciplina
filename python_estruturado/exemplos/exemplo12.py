# Implementar uma solução que calcule as raízes de uma equação do segundo grau
# Exemplo: dada a equação x^2+5x+6 = 0 as raízes são {-3, -2}
import numpy as np

def entrarDados():
    coeficiente = eval(input('Digite o valor do coeficiente:'))
    return coeficiente

def calcularDelta(a, b, c):
    delta = (b*b) - 4 * a * c
    return delta

def calcularRaizes(a, b, c, delta): 
    if(delta < 0): 
        resultado = 'A equação não possui raízes nos números reais'
    elif(delta == 0): 
        x = b / (2 * a)
        resultado = f'A equação possui apenas a raíz: {x}'
    else: 
        x1 = (-b - np.sqrt(delta))/(2 * a)
        x2 = (-b + np.sqrt(delta))/(2 * a)
        resultado = f'A equação possui duas raízes reais {x1} e {x2}'
    return resultado

a = entrarDados()
b = entrarDados()
c = entrarDados()
delta = calcularDelta(a, b, c)
resultado = calcularRaizes(a, b, c, delta)
print(resultado)
