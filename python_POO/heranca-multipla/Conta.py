from SaldoInsuficienteException import SaldoInsuficienteException

class Conta:
    def __init__(self, clientes, numero, saldo):
        self.clientes = clientes
        self.numero = numero
        self.saldo = saldo

    @property
    def saldo(self):
        return self._saldo
    
    @saldo.setter
    def saldo(self, saldo):
        if saldo < 0:
            print ("saldo inválido")
        else:
            self._saldo = saldo
    
    def depositar(self, valor):
        self.saldo += valor
    
    def sacar(self, valor):

        if(self.saldo < valor):
            raise SaldoInsuficienteException("Saldo insuficiente para realizar o saque")
        else:
            self.saldo -= valor 
            return True
    
    def transferirValor(self, contaDestino, valor):
        if self.saldo < valor:
           print("Não existe saldo suficiente")
        else:
           contaDestino.depositar(valor)
           self.saldo -= valor
        print("Transferencia Realizada") 