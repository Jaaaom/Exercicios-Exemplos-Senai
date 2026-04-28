class Carro:
    def __init__(self, marca, modelo, ano):  # Método Construtor preciso passar o modelo, ano, marca pois são atributos da classe Carro
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.ano})"

if __name__ == "__main__":
    carro1 = Carro("Toyota", "Corolla", 2020)

    print(carro1)