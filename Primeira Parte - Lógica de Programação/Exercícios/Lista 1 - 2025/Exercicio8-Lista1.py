# Escreva um algoritmo que leia três valores inteiros e diferentes e mostre-os em ordem descrescente

if __name__ == "__main__":

    vetor1 = []
    
    
    vetor1.insert(0, int(input("Insira um número inteiro: ")))
    vetor1.insert(1, int(input("Insira um número inteiro: ")))

    j=1
    while j==1:
        if vetor1[1] == vetor1[0]:
            vetor1.remove(vetor1[1])
            vetor1.insert(1, int(input("Insira um número inteiro diferente do primeiro: ")))
        else:
            j=0


    vetor1.insert(2, int(input("Insira um número inteiro: ")))
    j=1
    while j==1:
        if vetor1[2] == vetor1[0] or vetor1[2] == vetor1[1]:
            vetor1.remove(vetor1[2])
            vetor1.insert(2, int(input("Insira um número inteiro diferente do primeiro e do segundo: ")))
        else:
            j=0
    

    aux = vetor1[0]


    
    print(vetor1)
    vetor1.sort(reverse=True)

    print("Números em ordem decrescente:")
    print(vetor1)

