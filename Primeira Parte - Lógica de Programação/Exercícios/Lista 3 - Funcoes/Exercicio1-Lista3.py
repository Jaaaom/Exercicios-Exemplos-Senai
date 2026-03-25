# . Faça uma função que recebe por parâmetro o raio de uma esfera e calcula o seu volume  (v = 4/3.P .R3). 

def Calcular_volume(raio):
    volume = 3.14 * (raio**2)
    return volume

def main():
    raio = float(input("Digite o raio da esfera:"))

    volume = Calcular_volume(raio)

    print(volume)

if __name__ == "__main__":
    main()