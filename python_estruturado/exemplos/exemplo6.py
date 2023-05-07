# Implementar uma solução que resolva a seguinte questão: 
# Calcular o valor de uma compra, sendo que o preço unitário é R$10,00
# Se for feita uma compra de até 10 unidades, não há descontos
# Para compras entre 11 e 20 unidades é dado um desconto de 10%
# Acima de 20 unidades, é dado um desconto de 20%

precoUnit = 10.00
qntProduto = eval(input("Digite quantos produtos irá comprar:"))
if(qntProduto < 11): 
    desconto = 0
elif(qntProduto >= 11 and qntProduto <= 20):
    desconto = 0.1
elif(qntProduto > 20):
    desconto = 0.2

valorTotal = (precoUnit - (precoUnit * desconto)) * qntProduto

print(f'Você irá pagar R$ {valorTotal} com o desconto de {desconto * 100}%')