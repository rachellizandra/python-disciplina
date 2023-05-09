from Salario import Salario
from Empregado import Empregado

salario =  Salario(10000, 700, 100)
emp = Empregado('Musashi', 46, salario)
print(emp.salario_total())