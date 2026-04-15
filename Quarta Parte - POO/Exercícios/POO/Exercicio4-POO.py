# 4. Crie uma classe chamada ContaJogador com os atributos nickname e xp
# (experiência). Adicione os métodos:
# ● ganhar_xp(valor)
# ● gastar_xp(valor)
# ● exibir_status()

class ContaJogador:
    def __init__(self, nickname , xp):
        self.nickname = nickname
        self.xp = xp

    def ganhar_xp(self, valor):
        self.xp = self.xp + valor

    def gastar_xp(self,valor):
        self.xp = self.xp - valor

    def exibir_status(self):
        return f'Nick : {self.nickname} \nXP Atualizado: {self.xp}'

if __name__ == "__main__":
    jogador1 = ContaJogador('Shaolin Matador de Porco', 1500)
    print(jogador1.exibir_status())
    jogador1.ganhar_xp(250)
    print("Ganhou XP!!!")
    print(jogador1.exibir_status())
    print("======================================================================================")

    jogador2 = ContaJogador('Alanzoka', 2640)
    print(jogador2.exibir_status())
    jogador2.gastar_xp(320)
    print("Gastou XP!!!")
    print(jogador2.exibir_status())