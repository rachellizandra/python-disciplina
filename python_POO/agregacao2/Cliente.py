from Conta import Conta

class Cliente:
    def __init__(self, cpf, nome, endereco):
        self.cpf = cpf
        self.nome = nome
        self.endereco = endereco

def main():
    c1 = Cliente('1111111-1','Ana', 'Rua Pindamonhogaba. 27')
    c2 = Cliente('2222222-22', 'Carlos', 'Rua Canada, 128')
    conta1 = Conta([c1, c2], 24237891, 2500.00)
    conta2 = Conta([c1, c2], 2423555, 1000.00)
    conta1.depositar(1000)
    conta1.extrato.imprimir()
    conta1.transferirValor(conta2, 500.00)
    conta1.extrato.imprimir()

if __name__ == "__main__": 
    main()