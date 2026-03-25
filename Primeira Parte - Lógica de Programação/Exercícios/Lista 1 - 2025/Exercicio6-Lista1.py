# Escreva um algoritmo que lê dois valores boleanos (lógicos) e então determina se ambos são VERDADEIROS ou FALSOS

if __name__ == "__main__":

    num1 = str(input("Insira um valor lógico, isto é, 1 ou 0: "))
    num2 = str(input("Insira um valor lógico, isto é, 1 ou 0: "))

    if num1 == "1":
        print("VERDADEIRO")
    elif num1 == "0":
        print("FALSO")
    else:
        print("Valor lógico inválido!")

    if num2 == "1":
        print("VERDADEIRO")
    elif num2 == "0":
        print("FALSO")
    else:
        print("Valor lógico inválido! ")