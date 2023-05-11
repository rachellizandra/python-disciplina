# Considere a lista veiculos = ['aviao', 'carro', 'navio','onibus'] 
# Implementar uma solução através de programação funcional para trans todos os nomes em letras maiúsculas

veiculos = ['aviao', 'carro', 'navio','onibus']
letra_maiuscula = lambda x: str.upper(x)

nomes_maiusculos = list(map(letra_maiuscula, veiculos))

print(f'nomes maiúsculos = {nomes_maiusculos}')
