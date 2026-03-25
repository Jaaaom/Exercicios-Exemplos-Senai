#  Escreva um procedimento que recebe as 3 notas de um aluno por parâmetro e uma letra.  Se a letra for A o procedimento calcula a média aritmética das notas do aluno, se for P, a 
# sua média ponderada (pesos: 5, 3 e 2) e se for H, a sua média harmônica. A média  calculada também deve retornar por parâmetro.


def aluno(n1,n2,n3, letra):
    if letra.upper() == 'A':
        media_aritmetica = (n1+n2+n3)/3
        return media_aritmetica
    elif letra.upper() == 'P':
        media_ponderada = (n1*5+n2*3+n3*2)/10
        return media_ponderada
    elif letra.upper() == 'H':
        media_harmonica = 3/((1/n1)+(1/n2)+(1/n3))
        return media_harmonica
    
def main():
    media = input("Digite A - Média Aritmética , P - Ponderada , H - Harmõnica: ")

    match media.upper():
        case 'A':
            nota1 = float(input("Nota 1: "))
            nota2 = float(input("Nota 2: "))
            nota3 = float(input("Nota 3: "))
            print("Média aritmética = ", aluno(nota1,nota2,nota3,media))
        case 'P':
            nota1 = float(input("Nota 1: "))
            nota2 = float(input("Nota 2: "))
            nota3 = float(input("Nota 3: "))
            print("Média ponderada = ", aluno(nota1,nota2,nota3,media))
        case 'H':
            j = 0
            while j==0:
               nota1 = float(input("Nota 1 , essa nota deve ser diferente de zero: "))
               if nota1 == 0:
                   print("Nota inválida")
                   continue
               else:
                   j = 1
            j = 0
            while j==0:
               nota2 = float(input("Nota 2 , essa nota deve ser diferente de zero: "))
               if nota1 == 0:
                   print("Nota inválida")
                   continue
               else:
                   j = 1
            j = 0
            while j==0:
               nota3 = float(input("Nota 3 , essa nota deve ser diferente de zero: "))
               if nota1 == 0:
                   print("Nota inválida")
                   continue
               else:
                   j = 1
            print("Média Harmômica: ", aluno(nota1,nota2,nota3,media) )
        case _:
            pass
            

if __name__ == "__main__":
    main()

