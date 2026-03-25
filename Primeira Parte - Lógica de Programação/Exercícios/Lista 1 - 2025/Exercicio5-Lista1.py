#Encontrar o dobro de um número caso ele seja positivo e o seu triplo caso seja negativo, imprimindo o resultado

if __name__ == "__main__":

    num = float(input("Insira um número:"))

    if num >= 0:
        print("O dobro desse número é:", num*2)

    else:
        print("O triplo desse número é:", num*3)