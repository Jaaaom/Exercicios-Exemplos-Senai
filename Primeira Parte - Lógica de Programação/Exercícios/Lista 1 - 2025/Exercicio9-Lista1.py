# Tendo como dados de entrada a altura e o sexo de uma pessoa, construa um algoritmo
#que calcule seu peso ideal, utilizando as seguintes fórmulas:
#● para homens: (72.7 * h) – 58;
# ● para mulheres: (62.1 * h) – 44.7.

if __name__ == "__main__":
    altura = float(input("Qual a sua altura: "))
    sexo = input("Digite o sexo da pessoa (M/F): ")


    if sexo.upper() == 'M':
        print(" O peso ideal é: "(72.7*altura)-58)
    elif sexo.upper() == 'F':
        print(" O peso ideal é: ", (62.1*altura)-44.7, "kg")
    