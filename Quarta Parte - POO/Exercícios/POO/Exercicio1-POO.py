# 1. Crie uma classe chamada Personagem que tenha os atributos nome e poder.
# Instancie dois personagens e exiba seus dados no console.

class Personagem:
    def __init__(self,nome,poder):
        self.nome = nome
        self.poder = poder

    def __str__(self):
        return f'Nome: {self.nome} \n Poder : {self.poder}'
    
    def falar(self):
        return f'Mais de 8000!!!'
    
if __name__ == "__main__":
    personagem1 = Personagem('Megaman', 8001)
    personagem2 = Personagem('Napa', 1000)

    if personagem1.poder > 8000:
        print(personagem1.falar())