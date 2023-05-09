class Banco():
    def __init__(self, codigo,nome):
        self.codigo = codigo
        self.nome = nome
        self.contas = []

    def adicionaconta(self,contacliente):
        self.contas.append(contacliente)

    def calcularendimentomensal(self): #(7)
        for c in self.contas:
            c.CalculoRendimento()
            
    def imprimesaldocontas(self):
        for c in self.contas:
            print(c[0], c[1], c[3].strftime('%d/%b/%y'))