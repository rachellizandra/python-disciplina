class SaldoInsuficienteException(Exception):
    pass

class Conta:
    ...

    def sacar(self, valor):
        if self.saldo < valor:
            raise SaldoInsuficienteException("Saldo insuficiente para realizar o saque")
        else:
            self.saldo -= valor 
            return True