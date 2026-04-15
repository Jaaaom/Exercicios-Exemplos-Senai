# 3. Faça uma classe base Forma com um método area(). Crie subclasses Circulo e
# Retangulo que calculam a área corretamente. Use polimorfismo para imprimir a
# área de várias formas numa lista.

class Forma:
    def __init__(self, nome):
        self.nome = nome
    
    def area(self):
        raise NotImplementedError("Implemente nas subclasses")
    
class Circulo(Forma):
    def __init__(self, nome, raio):
        super().__init__(nome)
        self.raio = raio

    def area(self):
        area = 3.1415 * (self.raio)**2
        print(f"A área do {self.nome} de raio {self.raio} é {area:.2f}")

class Retangulo(Forma):
    def __init__(self, nome, base, altura):
        super().__init__(nome)
        self.base = base
        self.altura = altura

    def area(self):
        area = self.base*self.altura
        print(f"A área do {self.nome} de base {self.base} e altura {self.altura} é {area:.2f}")

if __name__ == "__main__":
    c = Circulo("Círculo", 10)
    r = Retangulo("Retângulo", 4,7)

    c.area()
    r.area()