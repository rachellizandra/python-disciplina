from Conta import Conta

class ContaEspecial(Conta):
    def __init__(self, clientes, numero, saldo, limite):
        super().__init__(clientes, numero, saldo)
        self.limite = limite

    def sacar(self, valor):
        if(self.saldo + self.limite) < valor:
            return False
        else: 
            self.saldo -= valor
            self.extrato.transacoes.append(["SAQUE", valor])
            return True