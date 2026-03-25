# Faça um algoritmo que leia 20 números e, ao final, escreva quantos estão entre 0 e 100.

if __name__ == "__main__":
    vetor_num = []

    for i in range (20):
        vetor_num.append(float(input("Insira um número: ")))
    
    cont = 0

    for i in range (20):
        if vetor_num[i] > 0 and vetor_num[i] < 100  :
            cont += 1
    
    print("Tem ", cont , "números entre 0 e 100")
