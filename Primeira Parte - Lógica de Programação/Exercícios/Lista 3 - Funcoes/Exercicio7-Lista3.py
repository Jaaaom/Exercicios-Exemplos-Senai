# . Faça uma função que verifique se um valor é perfeito ou não. Um valor é dito perfeito  quando ele é igual a soma dos seus divisores excetuando ele próprio. (Ex: 6 é perfeito, 6 = 
# 1 + 2 + 3, que são seus divisores). A função deve retornar um valor booleano.

def num_perfeito(num):
    soma = 0
    for i in range (1, num):
        if num%i  == 0:
            soma = soma + i
    
    if soma == num:
        return True
    
    else:
        return False

    

def main():
    numero = int(input("Insira um número inteiro: "))

    if num_perfeito(numero) == True:
        print("Número Perfeito:")
    else:
        print("Não é perfeito:")

if __name__ == "__main__":
    main()
    