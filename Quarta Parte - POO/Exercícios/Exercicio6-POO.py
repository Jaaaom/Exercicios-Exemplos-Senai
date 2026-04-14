# 6. Modifique a classe ContaJogador do exercício 4 para que o XP seja um atributo
# privado. Adicione:
# ● get_xp() para acessar o XP atual.

class ContaJogador:
    def __init__(self, nickname , xp):
        self.nickname = nickname
        self.__xp = xp

    def ganhar_xp(self, valor):
        self.__xp = self.__xp + valor

    def gastar_xp(self,valor):
        self.__xp = self.__xp - valor

    def exibir_status(self):
        return f'Nick : {self.nickname}'
    def get_xp(self):
        return f'XP: {self.__xp}'

if __name__ == "__main__":
    jogador1 = ContaJogador('Shaolin Matador de Porco', 1500)
    print(jogador1.exibir_status())
    print(jogador1.get_xp())
    jogador1.ganhar_xp(250)
    print("Ganhou XP!!!")
    print(jogador1.get_xp())
    print("======================================================================================")

    jogador2 = ContaJogador('Alanzoka', 2640)
    print(jogador2.exibir_status())
    print(jogador2.get_xp())
    jogador2.gastar_xp(320)
    print("Gastou XP!!!")
    print(jogador2.get_xp())