# Faça um algoritmo que leia dois valores inteiros A e B se os valores forem iguais deverá se somar os dois, caso contrário multiplique A por B.
# Ao final de qualquer um dos cálculos deve-se atribuir o resultado para uma variável C e mostrar seu conteúdo na tela

if __name__ == "__main__":

    A = int(input("Digite um número inteiro: "))
    B = int(input("Digite um número inteiro: "))
    
    if A == B:
        C = A+B
        print(" Os números são iguais logo a soma dos números é: ", C)
    else:
        C = A*B
        print(" Os números são diferentes logo o produto dos números é: ", C)