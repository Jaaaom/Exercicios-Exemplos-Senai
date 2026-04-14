# 2. Crie uma classe chamada Pokemon com os atributos nome e tipo. Crie um
# método chamado usar_ataque() que imprime na tela:
# ➝ "{nome} usou um ataque do tipo {tipo}!"

class Pokemom:
    def __init__(self,nome, tipo):
        self.nome = nome
        self.tipo = tipo

    def usar_ataque(self):
        return f'{self.nome} usou um ataque do tipo {self.tipo}'

if __name__ == "__main__":
    pokemom1 = Pokemom('Bulbassauro', 'Grama/Veneno')
    pokemom2 = Pokemom('Charmander', 'Fogo')
    pokemom3 = Pokemom('Squirtle', 'Água')
    pokemom4 = Pokemom('Pikachu', 'Elétrico')
    pokemom5 = Pokemom('gengar', 'Fantasma/Veneno')

    print(pokemom1.usar_ataque())
    print(pokemom2.usar_ataque())
    print(pokemom3.usar_ataque())
    print(pokemom4.usar_ataque())
    print(pokemom5.usar_ataque())