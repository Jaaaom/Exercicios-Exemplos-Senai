# Leia o nome e a idade de 10 pessoas e exiba o nome da pessoa mais nova.

if __name__ == "__main__":

    vetor_nome = []
    vetor_idade =[]

    for i in range (10):
        vetor_nome.append(input("Insira o nome da pessoa: "))
        vetor_idade.append(float(input("Insira a idade da pessoa: ")))

    idade_minima = vetor_idade[0]
    cont = 0

    for i in range (10):
        if idade_minima > vetor_idade[i]:
            idade_minima = vetor_idade[i]
            cont = i

    print(" A pessoa mais nova é: ", vetor_nome[cont])
    print(" Sua idade é: ", vetor_idade[cont])