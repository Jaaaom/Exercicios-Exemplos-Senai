# Faça uma função que recebe por parâmetro um valor inteiro e positivo e retorna o valor lógico Verdadeiro caso o valor seja primo e Falso em caso contrário.

def num_primo(num):
    cont = 0
    for i in range(num):
        if num%(i+1) == num or num%(i+1) == 0:
            cont += 1
    if cont == 2:
        return True
    else:
        return False

def main():
    numero = int(input("Insira um número inteiro: "))

    if num_primo(numero) == True:
        print("Número primo")
    else:
        print("Não é primo")

if __name__ == "__main__":
    main()