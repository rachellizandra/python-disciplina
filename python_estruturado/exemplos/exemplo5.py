# Implementar uma solução que resolva a seguinte questão: 
# Se nota for maior ou igual a 7, o estudante foi aprovado;
# Se nota for menor que 7 e maior ou igual a 5,5, o estudante está em recuperação
# Se a nota for menor que 5, o aluno está reprovado

nota = eval(input('Digite a nota final do aluno:'))
if (nota >= 7.0):
    situacao = "APROVADO"
elif(nota < 7.0 and nota >= 5.0):
    situacao = "EM RECUPERAÇÃO"
else:
    situacao = "REPROVADO"

print(f'O estudante está {situacao}')