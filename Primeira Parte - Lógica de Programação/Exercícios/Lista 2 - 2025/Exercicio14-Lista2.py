# Faça um algoritmo que leia 20 números e, ao final, escreva quantos estão entre 0 e 100, quantos estão entre 101 e 200 e quantos são maiores de 200.

if __name__ == "__main__":
    vetor_num = []

    for i in range (20):
        vetor_num.append(float(input("Insira um número: ")))
    
    cont = 0
    cont2 = 0
    cont3 = 0

    for i in range (20):
        if vetor_num[i] >= 0 and vetor_num[i] <= 100  :
            cont += 1
        elif vetor_num[i] >= 101 and vetor_num[i] <= 200:
            cont2 +=1
        elif vetor_num[i]> 200:
            cont3 +=1
    
    print("Tem ", cont , "números entre 0 e 100")
    print("Tem ", cont2 , "números entre 101 e 200")
    print("Tem ", cont3 , "números maiores que 200")