
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
