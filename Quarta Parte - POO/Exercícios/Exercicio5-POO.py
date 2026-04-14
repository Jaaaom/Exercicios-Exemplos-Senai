# 5. Crie uma classe Arena com os atributos largura e altura. Implemente os
# métodos:
# ● calcular_area() → retorna o tamanho total da arena.
# ● calcular_perimetro() → retorna o perímetro da arena.

class Arena:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
        self.area = 0
    def calcular_area(self):
        self.area = self.largura * self.altura
        return f'Área da Arena = {self.area} m^2'

    def calcular_perimetro(self):
        self.perimetro = (self.largura)*2 + (self.altura)*2
        return f'Perímetro da Arena = {self.perimetro} m^2'
    
if __name__ == "__main__":
    arena = Arena(3.5, 4)
    print(arena.calcular_area())
    print(arena.calcular_perimetro())