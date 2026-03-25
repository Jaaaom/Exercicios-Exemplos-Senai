#Elabore um algoritmo que calcule o que deve ser pago por um produto, considerando o preço normal de etiqueta e a escolha da condição de pagamento. Utilize os códigos da
# tabela a seguir para ler qual acondição de pagamento escolhida e efetuar o cálculo adequado.
# Código Condição de pagamento
# 1 À vista em dinheiro ou cheque, recebe 10% de desconto
# 2 À vista no cartão de crédito, recebe 15% de desconto
# 3 Em duas vezes, preço normal de etiqueta sem juros
# 4 Em duas vezes, preço normal de etiqueta mais juros de 10%

if __name__ == "__main__":

    preco = float(input("Preço do produto: "))
    condicao_pagamento = int (input("Insira o método de pagamento : 1 - À vista em dinheiro ou cheque , 2 À vista no cartão de crédito , 3 - Em duas vezes, 4 - Em duas vezes:  "))

    match condicao_pagamento:

        case 1: 
            print("Pagamento a vista no dinheiro ou cheque: Valor total R$", preco*0.9)
        case 2:
            print("Pagamento a vista no cartão: Valor total R$", preco*0.85)
        case 3:
            print("Pagamento em duas vezes sem juros: Valor total R$", preco)
        case 4:
            print("Pagamento em duas vezes com juros: Valor total R$", preco*1.1)
        case _:
            print("Método de pagamento imválido!")