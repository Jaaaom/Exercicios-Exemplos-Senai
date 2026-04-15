# 2. Implemente uma classe Funcionario com método calcular_bonus(). Crie subclasses Gerente e Vendedor que 
# sobrescrevam calcular_bonus() de formas diferentes.

class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def calcular_bonus(self):
        return "Sem bônus"
    
class Gerente(Funcionario):
    def calcular_bonus(self):
        return self.salario*1.2

class Vendedor(Funcionario):
    def calcular_bonus(self):
        return self.salario*1.15
    
if __name__ == "__main__":
    g = Gerente("Joana D'arc", 5000)
    v = Vendedor("Stuart", 2100)

    print(g.nome, " recebe R$", g.salario, "com o bônus fica R$", g.calcular_bonus())
    print(v.nome, " recebe R$", v.salario, "com o bônus fica R$", v.calcular_bonus())