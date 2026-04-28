# 5. Faça uma classe ContaBancaria com métodos depositar() e sacar(). Crie
# subclasses ContaPoupanca e ContaCorrente que sobrescrevam sacar()
# aplicando regras diferentes.

class ContaBancaria:
    def __init__(self, valor):
        self.valor = valor

    def depositar(self):
        raise NotImplementedError("Implemente nas subclasses")

    def sacar(self):
        raise NotImplementedError("Implemente nas subclasses")
    
class ContaPoupanca(ContaBancaria):

    def __init__(self, valor, dinheiro):
        super().__init__(valor)
        self.dinheiro = dinheiro

    def depositar(self):
        novo_valor = self.valor + self.dinheiro
        print("Você Depositou", self.dinheiro,"Saldo atual com o depoósito é de R$", novo_valor)
    
    def sacar(self):
        novo_valor = self.valor - self.dinheiro*1.05
        print("Você Sacou", self.dinheiro,"Saldo atual com desconto é de R$", novo_valor)
    
class ContaCorrente(ContaBancaria):
    def __init__(self, valor, dinheiro):
        super().__init__(valor)
        self.dinheiro = dinheiro

    def depositar(self):
        novo_valor = self.valor + self.dinheiro
        print("Você Depositou", self.dinheiro,"Saldo atual com o depoósito é de R$", novo_valor)
    
    def sacar(self):
        novo_valor = self.valor - self.dinheiro*1.1
        print("Você Sacou", self.dinheiro,"Saldo atual com desconto é de R$", novo_valor)

if __name__ == "__main__":
    cp = ContaPoupanca(45000, 2500)
    cp.depositar()
    cp.sacar()

    cc = ContaCorrente(12000, 1400)
    cc.depositar()
    cc.sacar()
