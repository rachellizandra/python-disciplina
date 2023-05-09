import datetime
from Extrato import Extrato

class Conta:
    def __init__(self, clientes, numero, saldo):
        self.clientes = clientes
        self.numero = numero
        self.saldo = saldo
        self.extrato = Extrato()

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
        self.extrato.transacoes.append(["DEPÓSITO", valor, "Data", datetime.datetime.today()])
    
    def sacar(self, valor):

        if(self.saldo < valor):
            return False
        else:
            self.saldo -= valor 
            self.extrato.transacoes.append(["SAQUE", valor, "Data", datetime.datetime.today()])
            return True
    
    def transferirValor(self, contaDestino, valor):
        if self.saldo < valor:
           print("Não existe saldo suficiente")
        else:
           contaDestino.depositar(valor)
           self.saldo -= valor
           self.extrato.transacoes.append(["TRANFERÊNCIA", valor, "Data", datetime.datetime.today()])
        print("Transferencia Realizada") 