# Escreva um algoritmo que leia uma sequência de números do usuário e realize a soma desses números. Encerre a execução quando um número negativo for digitado.

if __name__ == "__main__":

    soma = 0
    j = 1
    while j == 1:
        num = float(input("Insira um número, caso queira para digite um número negativo: "))

        if num >=0:
            soma = soma + num 
            continue
        else:
            print("Numero Negativo:")
            j = 0
    
    print(" A soma dos números digitados é: ", soma)