#  Escreva um algoritmo que leia o número de identificação, as 3 notas obtidas por um aluno nas 3 verificações e a média dos exercícios que fazem parte da avaliação, e calcule a 
#  média de aproveitamento, usando a fórmula: MA := (nota1 + nota 2 * 2 + nota 3 * 3 + ME)/7.
#  A atribuição dos conceitos obedece a tabela abaixo. O algoritmo deve escrever o número do  aluno, suas notas, a média dos exercícios, a média de aproveitamento, o conceito 
#  correspondente e a mensagem 'Aprovado' se o conceito for A, B ou C, e 'Reprovado' se o  conceito for D ou E. 
#       Média de aproveitamento Conceito 
#           >= 90 A 
#           >= 75 e < 90 B 
#           >= 60 e < 75 C 
#           >= 40 e < 60 D 
#           < 40 E

if __name__ == "__main__":
    num_identificacao = input("Insira o numero de indentificação do aluno: ")
    nota1 = float(input("Insira a nota 1: "))
    nota2 = float(input("Insira a nota 2: "))
    nota3 = float(input("Insira a nota 3: "))
    ME = float(input("Qual a média das notas dos exercícios: "))

    MA = (nota1 + nota2*2 + nota3*3 + ME)/7

    if MA >= 90:
        print("Conceito A")
    elif MA >= 75 and MA <90:
        print("Conceito B")
    elif MA>= 60 and MA<75:
        print("Conceito C")
    elif MA>= 40 and MA<60:
        print("Conceito D")
    elif MA>=0 and MA< 40:
        print("Conceito E")