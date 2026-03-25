#  Faça uma função que recebe por parâmetro o tempo de duração de uma fábrica expressa em segundos e retorna também por parâmetro esse tempo em horas, minutos e segundos.

def transformacao(seg):
    horas = seg//3600
    minutos = horas//60
    segundos = minutos%60

    return print(horas, "h", minutos, "m", segundos, "s")

def main():
    tempo = int(input("Informe o tempo em segundos: "))

    transformacao(tempo)

if __name__ == "__main__":
    main()