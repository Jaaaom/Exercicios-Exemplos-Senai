# . Faça uma função que recebe a idade de uma pessoa em anos, meses e dias e retorna essa idade expressa em dias.

def transformacao_dias(anos,meses,dias):
    if anos%4==0:
        return (anos/4)*366 + (anos - anos/4)