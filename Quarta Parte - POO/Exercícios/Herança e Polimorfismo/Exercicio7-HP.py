# 7. Crie uma classe InstrumentoMusical com método tocar(). Crie subclasses
# como Piano, Guitarra e Bateria com implementações diferentes para
# tocar(). Teste com uma lista de instrumentos.

class InstrumentoMusical:

    def __init__(self):
        pass

    def tocar(self):
        raise NotImplementedError("Implemente nas subclasses")
    
class Piano(InstrumentoMusical):
    def __init__(self):
        super().__init__()
        

    def tocar(self):
        print(""" O Piano é um instrumento que deve ser tocado sentado, caso ele 
              seja digital deve ligar em na tomada e em uma equipamento de som""")

class Guitarra(InstrumentoMusical):
    def __init__(self):
        super().__init__()
        

    def tocar(self):
        print(" A guitarra deve ser ligada em um amplificador para sair o som e toca usadno palheta")

class Bateria(InstrumentoMusical):
    def __init__(self):
        super().__init__()
        

    def tocar(self):
        print(" Se a bateria for eletrônica precisa de equipamento de som se for acústica é só tocar, tca usando baqueta")

if __name__ == "__main__":
    instrumentos = [Piano(), Guitarra(), Bateria()]

    for instr in instrumentos:
        instr.tocar()
