# Leia a idade de 20 pessoas e exiba quantas pessoas são maiores de idade.

if __name__ == "__main__":

    vetor_idade =[]

    for i in range (20):
        vetor_idade.append(float(input("Insira a idade da pessoa: ")))

    soma = 0
    for i in range (20):
        if vetor_idade[i] >= 18:
            soma += 1

    print("A quantidade de pessoas maiores de idade é : ", soma)