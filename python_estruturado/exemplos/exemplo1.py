# implemente uma solução que receba 2 numeros e identifique qual o maior deles
# numero1 = eval(input('Digite um numero:'))
# numero2 = eval(input('Digite outro numero:'))

# if (numero1 > numero2):
#     maior = numero1
#     print(f'O maior numero é {maior}')
# elif (numero2 > numero1):
#     maior = numero2
#     print(f'O maior numero é {maior}')
# else: 
#     print('Esses numeros são iguais')

# ou: 
numero1 = eval(input('Digite um numero:'))
numero2 = eval(input('Digite outro numero:'))
maior = numero1
if(numero2 > maior):
    maior = numero2
print(f'O maior numero é {maior}')
