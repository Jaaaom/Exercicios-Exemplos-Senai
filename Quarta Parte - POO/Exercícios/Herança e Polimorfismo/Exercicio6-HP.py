# 6 . Implemente uma hierarquia de classes para Funcionario onde cada funcionário
# tem um método descricao(). Crie subclasses e faça uma lista com vários
# funcionários, imprimindo as descrições usando polimorfismo.

class Funcionario:
    def __init__(self, nome):
        self.nome = nome

    def descricao(self):
        raise NotImplementedError("Implemente nas subclasses")
    
class Atendente(Funcionario):
    def __init__(self, nome, atribuicao):
        super().__init__(nome)
        self.atribuicao = atribuicao

    def descricao(self):
        print(f"\nCargo: Atendente \nNome: {self.nome} \nDescrição {self.atribuicao}")

class Caixa(Funcionario):
    def __init__(self, nome, atribuicao):
        super().__init__(nome)
        self.atribuicao = atribuicao

    def descricao(self):
        print(f"\nCargo: Caixa \nNome: {self.nome} \nDescrição {self.atribuicao}")

class Repositor(Funcionario):
    def __init__(self, nome, atribuicao):
        super().__init__(nome)
        self.atribuicao = atribuicao

    def descricao(self):
        print(f"\nCargo: Repositor \nNome: {self.nome} \nDescrição {self.atribuicao}")

if __name__ == "__main__":

    funcionario1 = Atendente('Roberto Carlos', " Atende os pedidos feitos pelos clientes")
    funcionario1.descricao()
    funcionario2 = Caixa('Michael Jackson', " Recolhe os pagamentos")
    funcionario2.descricao()
    funcionario3 = Repositor('Justin Bieber', " Repõe produtos no estoque")
    funcionario3.descricao()
    
