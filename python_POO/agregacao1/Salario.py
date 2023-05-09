class Salario:
    def __init__(self, nome, base, bonus):
        self.nome = nome
        self.base = base
        self.bonus = bonus

    def salario_anual(self):
        return (self.base * 12) + self.bonus