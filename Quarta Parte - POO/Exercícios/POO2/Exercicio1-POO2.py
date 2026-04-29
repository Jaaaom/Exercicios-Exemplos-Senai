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

    def atacar(self,alvo):
        dano = 100* self.nivel

        alvo.hp = alvo.hp - dano

class Mago(Personagem):
    def __init__(self, nome, hp, nivel):
        super().__init__(nome, hp, nivel)

    def atacar(self,alvo):
        dano = 80* self.nivel

        alvo.hp = alvo.hp - dano

class Arqueiro(Personagem):
    def __init__(self, nome, hp, nivel):
        super().__init__(nome, hp, nivel)

    def atacar(self,alvo):
        dano = 50* self.nivel

        alvo.hp = alvo.hp - dano

def batalha(p1,p2):
    pass


    