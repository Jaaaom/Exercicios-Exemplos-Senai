# Faça um algoritmo que leia o nome, sexo e o estado civil de uma pessoa. Caso sexo seja 'F' e estado civil  seja 'CASADA', solicitar o tempo de casada (anos)

if __name__ == "__main__":

    nome = str(input("Nome: "))
    sexo = str(input("Sexo: "))
    estado_civil = str(input("Estado Civil: "))

    if sexo.upper() == 'F' and estado_civil.upper() == 'CASADA':
        anos = int(input("Qual a sua idade: "))
        print("Nome:", nome)
        print("Sexo:", sexo)
        print("Estado Civil:", estado_civil)
        print("Idade:", anos)