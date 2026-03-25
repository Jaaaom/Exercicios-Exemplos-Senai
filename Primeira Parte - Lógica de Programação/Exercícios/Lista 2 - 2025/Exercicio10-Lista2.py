# Crie um algoritmo leia um número do usuário e exiba a sua tabuada de multiplicação.

if __name__ == "__main__":

    num = int(input("Insira um número inteiro: "))
    
    print(" A tabuada de ",num, "é")
    for i in range (10):
        print(num, "x" , i+1 , " = ", num * (i+1))