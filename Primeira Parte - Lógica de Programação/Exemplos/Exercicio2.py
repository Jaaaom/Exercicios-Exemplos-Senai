
if __name__ == "__main__":
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))

    media = (nota1 + nota2)/2

    print("A média é: ", media)
    print("A média é: {:.2f}".format(media)) # assim eu deixo o valor da média com duas casas decimais

    if media >7:
        print("Aprovado")

    else:
        print ("Reprovado")
