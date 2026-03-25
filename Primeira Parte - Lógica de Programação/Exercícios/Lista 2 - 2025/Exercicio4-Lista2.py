# Leia o nome um número do usuário um número N e escreva o nome dele na tela N vezes.

if __name__ == "__main__":

    nome = input("Qual seu nome: ")
    N = int(input("Insira um número inteiro positivo: "))

    for i in range (N):
        print(nome)