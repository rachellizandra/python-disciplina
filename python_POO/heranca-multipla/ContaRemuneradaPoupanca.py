from Poupanca import Poupanca
from Conta import Conta
from Cliente import Cliente

class ContaRemuneradaPoupanca(Conta, Poupanca):
    def __init__(self, clientes, numero, saldo, taxaremuneracao):
        super().__init__(self, clientes, numero, saldo)
        super().__init__(self, taxaremuneracao)
        self.taxaremuneracao = taxaremuneracao
    
    def remunerarConta(self):
        self.saldo += self.saldo * (self.taxaremuneracao / 30)
    

c1 = Cliente('1111111-1','Ana', 'Rua Pindamonhogaba. 27')
c2 = Cliente('2222222-22', 'Carlos', 'Rua Canada, 128')
cx = ContaRemuneradaPoupanca([c1, c2], 968539288, 1500.00, 0.03)
cx.remunerarConta()
print(cx.saldo)