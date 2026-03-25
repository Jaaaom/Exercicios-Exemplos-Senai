# O IMC – Indice de Massa Corporal é um critério da Organização Mundial de Saúde para dar uma indicação sobre a condição de peso de uma pessoa adulta.
# A fórmula é IMC = peso / ( altura )^2.
# Elabore um algoritmo que leia o peso e a altura de um adulto e mostre sua condição de acordo com a tabela abaixo.
# IMC em adultos Condição
# Abaixo de 18,5 Abaixo do peso
# Entre 18,5 e 25 Peso normal
# Entre 25 e 30 Acima do peso
# Acima de 30 obeso

if __name__ == "__main__":

    peso = float(input("Qual o seu peso: "))
    altura = float(input("Qual a sua altura: "))

    IMC = (peso) / (altura **2)

    if IMC < 18.5:
        print("Seu IMC é: ", IMC )
        print(" A pessoa está abaixo do peso: ")
    
    if IMC >= 18.5 and IMC < 25:
        print("Seu IMC é: ", IMC )
        print(" Peso Normal ")
    
    if IMC >= 25 and IMC < 30:
        print("Seu IMC é: ", IMC )
        print(" Acima do peso ")
    
    if IMC >=30:
        print("Seu IMC é: ", IMC )
        print(" Obeso")
    
    