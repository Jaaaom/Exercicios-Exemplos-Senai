# 3. Crie uma classe chamada NaveEspacial com os atributos nome, velocidade e vida. 
# Adicione um método exibir_status() que imprime esses dados no console.

class NaveEspacial:
    def __init__(self, nome, velocidade, vida):
        self.nome = nome
        self.velocidade = velocidade
        self.vida = vida

    def exibir_status(self):
        return f'Nave: {self.nome} \nVelocidade : {self.velocidade} \nVida: {self.vida}'

if __name__ == "__main__":
    nave = NaveEspacial('Milleniun Falcon' , '300.000 m/s' , 10000)

    print(nave.exibir_status())