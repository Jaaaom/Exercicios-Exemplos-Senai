# 1. Crie uma classe Veiculo com um método mover(). Depois crie classes Carro e
# Bicicleta que herdam de Veiculo e sobrescrevam o método mover() com
# comportamentos diferentes.

class Veiculo:
    def __init__(self, nome):

        self.nome = nome

    def mover(self):
            return " Movimento Retílineo"
        
class Carro(Veiculo):
    def mover(self):
        return "4 rodas"

class Bicicleta(Veiculo):
    def mover(self):
        return "2 rodas"
    
if __name__ == "__main__":
    c = Carro("Lamborghini Urus")
    b = Bicicleta("Caloi")

    print(c.nome, " tem " , c.mover())
    print(b.nome, " tem ", b.mover())