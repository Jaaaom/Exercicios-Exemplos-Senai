# 8. Crie uma classe Mensagem com método enviar(). Crie subclasses Email e SMS
# que sobrescrevam o método para enviar mensagens específicas. Faça uma função
# que envie uma lista mista de mensagens.

class Mensagem:
    def enviar(self):
        raise NotImplementedError("Implemente nas subclasses")
    
class Email(Mensagem):
    def __init__(self,destinatario, assunto, corpo):
        self.destinatario = destinatario
        self.assunto = assunto
        self.corpo = corpo

    def enviar(self):
        print(f"Envie um Email para {self.destinatario} \nAssunto: {self.assunto} \nCorpo: {self.corpo}")

class SMS(Mensagem):
    def __init__(self,numero, texto):
        self.numero = numero
        self.texto = texto

    def enviar(self):
        print(f"\nEnvie um SMS para o número {self.numero} \nTexto: {self.texto}")

if __name__ == "__main__":
    mensagens = [Email('joao.joao@gmail.com', 'Artigo', ' A data final par o artigo é 1 de Maio'), 
                 SMS('(24) 99999-8888', 'Seu pedido está a caminho, espere o entregador')]
    
    for msg in mensagens:
        msg.enviar()