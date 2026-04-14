# 7. Crie uma classe Inventario com os atributos privados nome, preco,peso e
# quantidade. Adicione métodos para:
# ● Alterar o preço (set_preco) somente se for maior que zero.
# ● Adicionar (adicionar_item) e remover itens (remover_item), sem
# permitir quantidade negativa.
# ● Exibir detalhes do item.

class Inventario:
    def __init__(self):
        self.__nome = None
        self.__preco = None
        self.__peso = None
        self.__quantidade = None

    def set_preco(self,valor):
        if valor > 0:
            self.__preco = valor
            return True
        return False

    def adicionar_item (self,nome, peso, quantidade, preco):
        if (peso<0) or (quantidade <0) or (preco <0):
            return False
        self.__nome = nome
        self.__peso = peso
        self.__quantidade =  quantidade

        if self.set_preco(preco):
            return True
        return False

    def remover_item(self, quantidade_nova):
        self.__nome = None
        self.__preco = None
        self.__peso = None
        self.__quantidade = None

    def exibir_detalhes(self):
        return f'Nome: {self.__nome} \nPeso : {self.__peso} \nPreço : {self.__preco} \nQuantidade: {self.__quantidade}'
        

if __name__ == "__main__":
    produto = Inventario()

    if produto.adicionar_item('PS5', 1.5, 25, 4599):
        print("Adiconando Item")

    produto.remover_item()

    print(produto.exibir_detalhes())

    