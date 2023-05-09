from datetime import date

class Pessoa:
    _contador = 0

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        Pessoa._contador += 1
    
    @classmethod
    def apartirAnoNascimento(cls, nome, ano):
        return cls(nome, date.today().year - ano)

    @staticmethod
    def ehMaiorIdade(idade):
        return idade >= 18
    
    @property
    def contador(self):
        return type(self)._contador

pessoa1 = Pessoa('maria', 26)
pessoa2 = Pessoa.apartirAnoNascimento('ana', 2006)
print(pessoa1.idade)
print(pessoa2.idade)
print(pessoa1.contador)
print(Pessoa._contador)