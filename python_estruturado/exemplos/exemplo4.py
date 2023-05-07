# Implementar uma solução que verifique se um número é par ou ímpar
numero = eval(input('Digite um numero:'))
if (numero % 2 == 0):
    print(f'{numero} é par')
else: 
    print(f'{numero} é impar')