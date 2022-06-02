

def calcular_calorias_en_reposo(peso, altura, edad, genero):

    if(genero == 'M'):
        valor_genero = 5
    else:
        valor_genero = -161

    tmb = (10 * peso) + (6.25 * altura) - (5 * edad) + valor_genero
    return round(tmb)
