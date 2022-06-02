
print('Bienvenido.')
peso = float(input('Ingrese su peso: '))
altura = float(input('Ingrese su altura: '))
edad = int(input('Ingrese su edad: '))
genero = input('Ingrese su genero: (F o M) ')
actividadFisica = int(input('Indique grado de actividad realizada: (1) Poco o ninguno, (2) Ejercicio ligero, (1 a 3 dias a la semana), (3) Ejercicio moderado (3 a 5 dias a la semana), (4) Deportista (6 a 7 dias a la semana), (5) Atleta (Entrenamiento manana y tarde) '))


def calcular_porcentaje_grasa(IMC, edad, genero):
    if(genero == 'F'):
        valor_genero = 10.8
    else:
        valor_genero = 0
    Gc = 1.2 * IMC + 0.23 * edad - 5.4 - valor_genero
    return round(Gc)


def calcular_IMC(peso, altura):
    Imc = peso / (altura * altura)
    return round(Imc)


def valor_actividad(actividadFisica):
    if(actividadFisica == 1):
        return 1.2

    elif(actividadFisica == 2):
        return 1.375
    elif(actividadFisica == 3):
        return 1.55
    elif(actividadFisica == 4):
        return 1.72
    elif(actividadFisica == 5):
        return 1.9


def calcular_calorias_en_actividad(TMB, actividadFisica):
    nuevoValorActividad = valor_actividad(actividadFisica)
    return round(TMB * nuevoValorActividad)

def calcular_calorias_en_reposo(peso, altura, edad, genero):

    if(genero == 'M' or genero == "m"):
        valor_genero = 5
    else:
        valor_genero = -161

    tmb = (10 * peso) + (6.25 * altura) - (5 * edad) + valor_genero
    return round(tmb)
   

def consumo_calorias_recomendado_para_adelgazar(TMB):
    Tmbmin = (TMB * 80) / 100
    Tmbmax = (TMB * 85) / 100

    return 'Para adelgazar es recomendado que consumas entre', round(Tmbmin), ' y ', round(Tmbmax), 'calorias'
