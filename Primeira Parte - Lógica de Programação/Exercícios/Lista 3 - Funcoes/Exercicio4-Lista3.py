# Faça um procedimento que recebe por parâmetro os valores necessário para o cálculo da  fórmula de báskara e retorna, também por parâmetro, as suas raízes, caso seja possível 
# calcular.


def baskara(a,b,c):
    if (b**2) - 4*a*c <0:
        print("Não tem raiz real: ")
    else:
        raiz1 = ((-1)*b + ((b**2) - 4*a*c)**0.5)/(2*a)
        raiz2 = ((-1)*b - ((b**2) - 4*a*c)**0.5)/(2*a)

    return(raiz1, raiz2)

def main():
    print("Dado que uma função de segundo grau é dado por ax^2 + bx + c")
    a = float(input("Valor de a: "))
    b = float(input("Valor de b: "))
    c = float(input("Valor de c: "))

    print("As raízes da sua função são: ", baskara(a,b,c))


if __name__ == "__main__":
    main()