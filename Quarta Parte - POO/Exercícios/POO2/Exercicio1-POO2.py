# 1. Crie uma hierarquia de classes para um mini-RPG: uma classe
# abstrata Personagem com os atributos nome , hp e nivel , e o método
# abstrato atacar(alvo) . Implemente as subclasses Guerreiro , Mago e Arqueiro ,
# cada uma com seu próprio cálculo de dano. Ao final, simule uma batalha em
# loop onde dois personagens se atacam alternadamente até um deles cair.


class Personagem:
    def __init__(self, nome, hp, nivel):
        self.nome = nome
        self.hp = hp
        self.nivel = nivel

    def atacar(self):
        raise NotImplementedError("Implemente nas subclasses")
    

class Guerreiro(Personagem):
    def __init__(self, nome, hp, nivel):
        super().__init__(nome, hp, nivel)

class Mago(Personagem):
    def __init__(self, nome, hp, nivel):
        super().__init__(nome, hp, nivel)

class Arqueiro(Personagem):
    def __init__(self, nome, hp, nivel):
        super().__init__(nome, hp, nivel)

    