# Escreva um algoritmo que leia 20 números do usuário e exiba quantos números são pares

if __name__ == "__main__":
    vetor_num = []

    for i in range (20):
        vetor_num.append(float(input("Insira um número: ")))
    
    cont = 0

    for i in range (20):
        if vetor_num[i] % 2 == 0:
            cont += 1
    
    print("Tem ", cont , "números pares")