# Leia a idade de 20 pessoas e exiba a soma das idades.

if __name__ == "__main__":

    vetor_idade =[]

    for i in range (20):
        vetor_idade.append(float(input("Insira a idade da pessoa: ")))

    soma = 0
    for i in range (20):
        soma = soma + vetor_idade[i]

print("A soma das idades é: ", soma)