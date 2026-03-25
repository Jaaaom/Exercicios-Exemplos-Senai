# Faça um algoritmo que leia os valores A,B,C e impirma na tela a soma de A+B é menor que C

if __name__ == "__main__":

    A = float(input("Digite um número: "))
    B = float(input("Digite um número: "))
    C = float(input("Digite um número: "))

    if A+B < C:
        print("A+B é menor que C")
