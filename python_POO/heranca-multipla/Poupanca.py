from datetime import datetime
from Conta import Conta

class Poupanca:
    def __init__(self, saldo, taxaremuneracao):
        self.saldo = saldo
        self.taxaremuneracao = taxaremuneracao
        self.data_abertura = datetime.today()

    def remunerarConta(self):
        self.saldo += self.saldo * self.taxaremuneracao
