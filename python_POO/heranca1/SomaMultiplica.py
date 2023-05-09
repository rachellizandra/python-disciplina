class SomaMultiplica: 
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def somar(self):
        return self.a + self.b
    
    def multiplicar(self):
        return self.a * self.b

class Derivada(SomaMultiplica):
    def subtrair(self):
        return self.a - self.b
    
    def dividir(self):
        if (self.b != 0):
            return self.a / self.b
        else: 
            return ZeroDivisionError

d = Derivada(10, 20)
print({d.somar()})
print(issubclass(Derivada, SomaMultiplica))
