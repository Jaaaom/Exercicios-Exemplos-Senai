# 4. Crie uma classe Animal com um método fazer_som(). Crie subclasses
# Cachorro, Gato e Passaro que implementem sons diferentes. Faça uma função
# que receba um animal e chame fazer_som() sem saber qual classe é.

class Animal:
    def fazer_som(self):
        raise NotImplementedError("Implemente nas subclasses")
    
class Cachorro(Animal):
    
    def fazer_som(self):
        return "Au Au"
class Gato(Animal):
    
    def fazer_som(self):
        return "Miau"

class Passaro(Animal):
    
    def fazer_som(self):
        return "Piu Piu"

def som_animal(nome):
    print(nome.fazer_som())

if __name__ == "__main__":
    pets = [Cachorro(), Gato(), Passaro()]

    for pet in pets:
        som_animal(pet)