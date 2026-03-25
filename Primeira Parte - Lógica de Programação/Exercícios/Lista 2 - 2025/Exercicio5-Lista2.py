# Escreva um algoritmo que leia 10 números do usuário e calcule a soma desses números.

if __name__ == "__main__":
    vetor = []

for i in range (10):
    vetor.append(float(input("Insira um número: ")))

soma = 0

for i in range (10):
    soma = soma + vetor[i]

print("A soma dos valores digitados é: ", soma)