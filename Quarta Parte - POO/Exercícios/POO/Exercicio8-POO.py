# 8. Crie uma classe SensorDeKi com um atributo privado nivel_ki. Permita:
# ● Ler o nível de ki (get_ki()).
# ● Alterar o ki (set_ki()) apenas se o valor estiver entre 0 e 9000. Se passar de
# 8000, imprima:
# ➝ “é mais de 8000!!!”

class SensorDeKi:
    def __init__(self, nivel_ki):
        self.__nivel_ki = nivel_ki
        self.set_ki(nivel_ki)

    def get_ki(self):
        return self.__nivel_ki
    
    def set_ki(self, valor):
        if valor>= 0 and valor <= 9000:
            self.__nivel_ki = valor
            if valor > 8000:
                print("É mais de 8000!!!!!!!!!!!!!!!")
        else:
            print("Valor inválido! O ki deve estar entre 0 e 9000.")


if __name__ == "__main__":

    ki = SensorDeKi(5500)
    print("ki = ", ki.get_ki())

    ki.set_ki(8500)
    print("ki = ", ki.get_ki())

    ki.set_ki(9700)
    